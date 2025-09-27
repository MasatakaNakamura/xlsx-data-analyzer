#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import re
import sys

def load_shared_strings(shared_strings_file):
    """共有文字列ファイルを読み込んで辞書に格納"""
    shared_strings = {}
    try:
        tree = ET.parse(shared_strings_file)
        root = tree.getroot()

        # 名前空間の定義
        namespaces = {'': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

        for i, si in enumerate(root.findall('.//si', namespaces)):
            text_parts = []
            # テキスト要素を取得
            for t in si.findall('.//t', namespaces):
                if t.text:
                    text_parts.append(t.text)

            if text_parts:
                shared_strings[i] = ''.join(text_parts)
    except Exception as e:
        print(f"Error loading shared strings: {e}")

    return shared_strings

def parse_worksheet(worksheet_file, shared_strings):
    """ワークシートファイルを解析してセルデータを取得"""
    try:
        tree = ET.parse(worksheet_file)
        root = tree.getroot()

        # 名前空間の定義
        namespaces = {'': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

        cells = {}

        # セルデータを取得
        for row in root.findall('.//row', namespaces):
            for cell in row.findall('.//c', namespaces):
                cell_ref = cell.get('r')  # A1, B2などのセル参照
                cell_type = cell.get('t', '')  # セルタイプ

                value_elem = cell.find('.//v', namespaces)
                if value_elem is not None and value_elem.text:
                    value = value_elem.text

                    # 共有文字列の場合は変換
                    if cell_type == 's':
                        try:
                            string_index = int(value)
                            if string_index in shared_strings:
                                value = shared_strings[string_index]
                        except (ValueError, KeyError):
                            pass

                    cells[cell_ref] = value

        return cells
    except Exception as e:
        print(f"Error parsing worksheet: {e}")
        return {}

def cells_to_table(cells):
    """セルデータをテーブル形式に変換"""
    if not cells:
        return []

    # セル参照を行列に変換
    cell_positions = {}
    max_row = 0
    max_col = 0

    for cell_ref, value in cells.items():
        match = re.match(r'([A-Z]+)(\d+)', cell_ref)
        if match:
            col_str, row_str = match.groups()
            row = int(row_str)
            col = 0
            for char in col_str:
                col = col * 26 + (ord(char) - ord('A') + 1)

            cell_positions[(row, col)] = value
            max_row = max(max_row, row)
            max_col = max(max_col, col)

    # テーブルを構築
    table = []
    for row in range(1, max_row + 1):
        row_data = []
        for col in range(1, max_col + 1):
            value = cell_positions.get((row, col), '')
            row_data.append(str(value))
        table.append(row_data)

    return table

def table_to_markdown(table, sheet_name):
    """テーブルをMarkdown形式に変換"""
    if not table:
        return f"# {sheet_name}\n\n（空のシート）\n"

    markdown = f"# {sheet_name}\n\n"

    if table:
        # 空の行を除去
        non_empty_rows = []
        for row in table:
            if any(cell.strip() for cell in row):
                non_empty_rows.append(row)

        if non_empty_rows:
            # 最大列数を計算
            max_cols = max(len(row) for row in non_empty_rows)

            # テーブルヘッダー
            markdown += "| " + " | ".join([f"列{i+1}" for i in range(max_cols)]) + " |\n"
            markdown += "| " + " | ".join(["---" for _ in range(max_cols)]) + " |\n"

            # データ行
            for i, row in enumerate(non_empty_rows):
                # 行を最大列数に合わせる
                padded_row = row + [''] * (max_cols - len(row))
                # セル内の改行をスペースに変換
                cleaned_row = [cell.replace('\n', ' ').replace('\r', ' ').strip() for cell in padded_row]
                markdown += "| " + " | ".join(cleaned_row) + " |\n"

    return markdown

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python excel_parser.py <worksheet_file> <shared_strings_file> <output_file>")
        sys.exit(1)

    worksheet_file = sys.argv[1]
    shared_strings_file = sys.argv[2]
    output_file = sys.argv[3]

    # ファイル名からシート名を取得
    sheet_name = "Sheet"
    if "sheet1" in worksheet_file:
        sheet_name = "TGシート"
    elif "sheet2" in worksheet_file:
        sheet_name = "GGシート"
    elif "sheet3" in worksheet_file:
        sheet_name = "構成図シート"

    print(f"Loading shared strings from {shared_strings_file}...")
    shared_strings = load_shared_strings(shared_strings_file)
    print(f"Found {len(shared_strings)} shared strings")

    print(f"Parsing worksheet {worksheet_file}...")
    cells = parse_worksheet(worksheet_file, shared_strings)
    print(f"Found {len(cells)} cells")

    print("Converting to table...")
    table = cells_to_table(cells)
    print(f"Table dimensions: {len(table)} rows")

    print("Converting to markdown...")
    markdown = table_to_markdown(table, sheet_name)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"Markdown saved to {output_file}")