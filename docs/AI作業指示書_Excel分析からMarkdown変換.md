# AI作業指示書 - Excel分析からMarkdown変換プロセス

## 📋 作業概要

Excelファイルをzipとして展開・分析し、各シートの内容を人間が見やすいMarkdown形式に変換する作業の詳細手順書

---

## 🎯 作業目標

- Excelファイル（経歴書等）の内容を構造化されたMarkdownドキュメントに変換
- 図表が必要な箇所はmermaid形式で作成
- 人間が理解しやすい形式での情報整理
- 分析結果の総合レポート作成

---

## 📂 前提条件

### 作業環境
- docsディレクトリへの書き込み権限
- mermaid図の作成能力
- 日本語での文書作成

---

## 🔄 作業フロー

### Phase 0: Excel解析・展開フェーズ（前処理）

#### Step 0-1: タスク管理の初期化（解析フェーズ）
```markdown
TodoWriteツールを使用して以下のタスクを設定：
1. Excelファイルの拡張子を.xlsxから.zipに変換
2. zipファイルをunzipして展開
3. 展開されたディレクトリ構造を分析
4. excel_structure_analysis.mdを作成
5. 各シートのXX_sheet.mdファイルを作成
```

#### Step 0-2: Excelファイルの拡張子変換【1番目のタスクを in_progress に設定】

**対象ファイル**: `*.xlsx`
**操作**: 拡張子を`.xlsx`から`.zip`に変更

```bash
# ファイル名例：経歴書サンプル.xlsx → 経歴書サンプル.zip
cp "経歴書サンプル.xlsx" "経歴書サンプル.zip"
```

**重要な注意事項**:
- ファイル名にスペースや日本語が含まれる場合は必ずクォートで囲む
- バックアップとして元ファイルのコピーを保持推奨
- 作業ディレクトリの確認を事前に実行

**完了後**: タスクをcompletedに変更

#### Step 0-3: zipファイルの展開【2番目のタスクを in_progress に設定】

**操作**: zipファイルを展開してディレクトリ構造を作成

```bash
# 展開先ディレクトリを作成
mkdir -p "展開用ディレクトリ"
# zipファイルを展開
unzip "経歴書サンプル.zip" -d "展開用ディレクトリ/"
```

**展開後の期待構造**:
```
展開用ディレクトリ/
├── [Content_Types].xml
├── _rels/
│   └── .rels
├── docProps/
│   ├── app.xml
│   ├── core.xml
│   └── custom.xml
└── xl/
    ├── _rels/
    ├── calcChain.xml
    ├── drawings/
    ├── sharedStrings.xml
    ├── styles.xml
    ├── workbook.xml
    └── worksheets/
        ├── sheet1.xml
        ├── sheet2.xml
        └── sheet3.xml
```

**完了後**: タスクをcompletedに変更

#### Step 0-4: ディレクトリ構造の分析【3番目のタスクを in_progress に設定】

**分析対象**:
1. **ルートディレクトリ構造**: `ls -la`で全体を確認
2. **xlディレクトリ**: `ls -la xl/`でExcel本体構造を確認
3. **worksheetsディレクトリ**: `ls -la xl/worksheets/`でシート一覧を確認
4. **共有文字列**: `xl/sharedStrings.xml`の内容確認
5. **ワークブック定義**: `xl/workbook.xml`でシート名・ID確認

**実行コマンド例**:
```bash
# ディレクトリ構造の確認
find "展開用ディレクトリ" -type f -name "*.xml" | head -20
# ワークシート一覧の確認
ls -la "展開用ディレクトリ/xl/worksheets/"
```

**完了後**: タスクをcompletedに変更

#### Step 0-5: excel_structure_analysis.md作成【4番目のタスクを in_progress に設定】

**出力ファイル**: `docs/excel_structure_analysis.md`

**必須含有要素**:
```markdown
# Excelファイル構造分析レポート - [ファイル名]

## 1. 概要
## 2. ファイル構造
### 2.1 ルートディレクトリ構造
### 2.2 Excelファイル構造図（Mermaid）
## 3. ドキュメント情報
### 3.1 基本情報（docProps/core.xml より）
### 3.2 アプリケーション情報（docProps/app.xml より）
### 3.3 ワークシート構成
## 4. 内容分析
### 4.1 共有文字列（sharedStrings.xml より抽出）
### 4.2 技術スタック構成図（Mermaid）
## 5. ワークシート詳細分析
## 6. 外部参照
## 7. まとめ
```

**重要なmermaid図**:
- ファイル構造図（graph TD形式）
- 技術スタック図（mindmap形式）
- プロセスフロー図（必要に応じて）

**完了後**: タスクをcompletedに変更

#### Step 0-6: 各シートファイルの作成【5番目のタスクを in_progress に設定】

**作成対象**: 各worksheet XMLファイルに対応するMarkdownファイル

**ファイル命名規則**:
- `sheet1.xml` → `docs/シート名_sheet.md`
- `sheet2.xml` → `docs/シート名_sheet.md`
- `sheet3.xml` → `docs/シート名_sheet.md`

**必須含有要素（各シートファイル）**:
```markdown
# [シート名]シート

## データ構造
- 表形式でのデータ表現
- 重要なセル値の抽出
- 数式・計算式の説明

## 特徴的な要素
- 条件付き書式
- データ検証
- 図形・グラフ（該当する場合）

## 業務的意味
- データの用途説明
- 関連するビジネスプロセス
```

**データ抽出方法**:
1. XMLファイルの`<c>`タグから値を抽出
2. `sharedStrings.xml`を参照して文字列を解決
3. 数式は`<f>`タグから取得
4. 表形式（Markdownテーブル）で整理

**完了後**: タスクをcompletedに変更

---

### Phase 1: 準備・分析フェーズ

#### Step 1-1: タスク管理の初期化（変換フェーズ）
```markdown
TodoWriteツールを使用して以下のタスクを設定：
1. TGシートの経歴書データを見やすいMarkdown形式で整理
2. GGシートの経歴書データを見やすいMarkdown形式で整理
3. 構成図シートのフローチャートをmermaid形式で改善
4. 全体のサマリーとプロジェクト分析ドキュメントを作成

※ Phase 0で作成された基本ファイル（excel_structure_analysis.md, XX_sheet.md）が前提
```

#### Step 1-2: 基準ファイルの確認
- `docs/20250927_001.md`を読み込み、作業対象を把握
- 既存のmarkdownファイル一覧を確認（mcp__serena__list_dir使用）

#### Step 1-3: 既存データの読み込み
以下のファイルを並行して読み込み：
- `docs/TG_sheet.md`
- `docs/GG_sheet.md`
- `docs/構成図_sheet.md`
- `docs/excel_structure_analysis.md`

---

### Phase 2: 個別シート変換フェーズ

#### Step 2-1: TGシート変換【最初のタスクを in_progress に設定】

**出力ファイル**: `docs/TG_経歴書_詳細.md`

**必須含有要素**:
```markdown
# TG（銀河 太郎）- 経歴書詳細

## 📋 基本情報
- 表形式での基本情報整理

## 💼 プロジェクト履歴
- 各プロジェクトを時系列で詳細化
- システム概要、作業内容、使用技術を構造化

## 📊 キャリア統計
- 業界経験のpieチャート（mermaid）
- 技術スキルのmindmap（mermaid）
- キャリア進展のtimeline（mermaid）
```

**完了後**: タスクをcompletedに変更

#### Step 2-2: GGシート変換【2番目のタスクを in_progress に設定】

**出力ファイル**: `docs/GG_経歴書_詳細.md`

**必須含有要素**:
```markdown
# GG（銀河 次郎）- 経歴書詳細

## 📋 基本情報
## 💼 プロジェクト履歴
## 🔍 TGとの比較分析  ← 重要：比較表を作成
## 📊 キャリア統計
## 🚀 今後の展望
```

**完了後**: タスクをcompletedに変更

#### Step 2-3: 構成図シート変換【3番目のタスクを in_progress に設定】

**出力ファイル**: `docs/構成図_詳細フローチャート.md`

**必須含有要素**:
```markdown
# 構成図シート - 詳細フローチャート分析

## 🔄 基本フローチャート
- 改善されたmermaidフローチャート

## 🎯 詳細プロセス分析
- サブグラフを使った詳細化

## 📈 データフロー図
- システム間連携図

## ⏱️ タイムライン処理フロー
- timeline図での時系列表現

## 🔧 エラーハンドリングフロー
- 例外処理フロー

## 📋 配置情報詳細
- Excel座標系での配置説明
```

**完了後**: タスクをcompletedに変更

---

### Phase 3: 総合分析レポート作成フェーズ

#### Step 3-1: 総合レポート作成【4番目のタスクを in_progress に設定】

**出力ファイル**: `docs/経歴書サンプル_総合分析レポート.md`

**必須含有要素**:
```markdown
# 経歴書サンプル.xlsx - 総合分析レポート

## 📋 エグゼクティブサマリー
## 👥 人材プロファイル比較
## 📊 プロジェクト履歴分析
## 💼 技術スキル進化分析
## 🏢 業界特化スキル分析
## 🎨 フローチャート設計分析
## 📈 キャリア進展パターン分析
## 🔍 組織戦略分析
## 📊 定量分析結果
## 🚀 今後の展開提案
## 📋 結論
```

**重要なmermaid図**:
- 人材プロファイル比較図
- 業界別経験分布（pie）
- 技術習得タイムライン（timeline）
- ガントチャート（プロジェクト期間）
- 技術スタック深度分析（mindmap）

**完了後**: タスクをcompletedに変更

---

## 📐 品質基準

### ドキュメント構造
- **ヘッダー階層**: 適切な#レベルの使用
- **絵文字活用**: 視認性向上のため各セクションにアイコン
- **表形式**: 比較データは必ず表形式で記載
- **コードブロック**: 技術情報は適切にマークアップ

### mermaid図の品質基準
```markdown
必須要素：
- スタイリング（fill, stroke, color指定）
- 適切な図表タイプの選択
  - flowchart: プロセスフロー
  - pie: 分布データ
  - timeline: 時系列データ
  - mindmap: 階層構造
  - gantt: スケジュール
  - graph: 関係図
- 日本語ラベルの適切な使用
```

### 内容の正確性
- **データの一貫性**: 全ドキュメント間での数値統一
- **技術用語**: 正確な技術表記
- **時系列**: 正確な期間計算（月数等）

---

## 🚨 注意事項

### 作業中の必須行動
1. **タスク管理**: 各フェーズでTodoWriteツールを必ず使用
2. **並行読み込み**: 複数ファイルは並行してRead実行
3. **段階的完了**: 1つのタスクが完了したら即座にcompletedに変更

### 避けるべき行動
- タスク管理なしでの作業開始
- 単一ファイルずつの逐次読み込み
- mermaid図なしでの図表表現
- 生データのコピー&ペーストのみ

---

## 🎯 成功指標

### 完了条件
**Phase 0（Excel解析）**:
- [ ] Excelファイルの拡張子変換完了
- [ ] zipファイルの展開完了
- [ ] excel_structure_analysis.mdの作成完了
- [ ] 各シートのXX_sheet.mdファイル作成完了
- [ ] 全Phase 0タスクがcompletedステータス

**Phase 1以降（Markdown変換）**:
- [ ] 4つの詳細markdownファイルが作成済み
- [ ] 各ファイルに適切なmermaid図が含まれている
- [ ] 人間が読みやすい構造化された内容
- [ ] 全タスクがcompletedステータス

### 品質チェックポイント
**Phase 0（Excel解析）**:
- [ ] ファイル拡張子変換の正確性
- [ ] zip展開の完全性（エラーなし）
- [ ] XML構造解析の正確性
- [ ] シートデータ抽出の完全性

**Phase 1以降（Markdown変換）**:
- [ ] データの数値的整合性
- [ ] mermaid図の視覚的品質
- [ ] 日本語表記の適切性
- [ ] 構造化された情報整理

---

## 🔄 実行コマンド例

### Phase 0開始時（Excel解析）
```markdown
TodoWriteツール実行：
[
  {"content": "Excelファイルの拡張子を.xlsxから.zipに変換", "status": "pending", "activeForm": "..."},
  {"content": "zipファイルをunzipして展開", "status": "pending", "activeForm": "..."},
  {"content": "展開されたディレクトリ構造を分析", "status": "pending", "activeForm": "..."},
  {"content": "excel_structure_analysis.mdを作成", "status": "pending", "activeForm": "..."},
  {"content": "各シートのXX_sheet.mdファイルを作成", "status": "pending", "activeForm": "..."}
]
```

### Phase 1開始時（Markdown変換）
```markdown
TodoWriteツール実行：
[
  {"content": "TGシートの経歴書データを見やすいMarkdown形式で整理", "status": "pending", "activeForm": "..."},
  {"content": "GGシートの経歴書データを見やすいMarkdown形式で整理", "status": "pending", "activeForm": "..."},
  {"content": "構成図シートのフローチャートをmermaid形式で改善", "status": "pending", "activeForm": "..."},
  {"content": "全体のサマリーとプロジェクト分析ドキュメントを作成", "status": "pending", "activeForm": "..."}
]
```

### ファイル読み込み（並行実行）
```markdown
Read: docs/20250927_001.md
Read: docs/TG_sheet.md
Read: docs/GG_sheet.md
Read: docs/構成図_sheet.md
（上記を同一メッセージ内で並行実行）
```

### Excel解析フェーズ実行コマンド
```bash
# 拡張子変更
mv "*.xlsx" "*.zip"

# 展開
mkdir extracted_excel
unzip "*.zip" -d "extracted_excel/"

# 構造確認
ls -la extracted_excel/
ls -la extracted_excel/xl/worksheets/
```

### ファイル作成（Phase 0）
```markdown
Write: docs/excel_structure_analysis.md
Write: docs/シート名_sheet.md （各シート分）
```

### ファイル作成（Phase 1以降）
```markdown
Write: docs/TG_経歴書_詳細.md
Write: docs/GG_経歴書_詳細.md
Write: docs/構成図_詳細フローチャート.md
Write: docs/経歴書サンプル_総合分析レポート.md
```

---

## 📝 応用・カスタマイズ指針

### 他のExcelファイル対応時
1. **基準ファイル**: `docs/YYYYMMDD_NNN.md`を確認
2. **Excel解析**: Phase 0の手順を必ず実行
3. **シート数**: 3シート以外の場合は適宜タスクを調整
4. **データ種別**: 経歴書以外の場合は出力構造を調整
5. **ファイル命名**: 元ファイル名に応じてmarkdownファイル名を調整

### 追加分析項目
- 技術トレンド分析
- リスク評価
- 競合比較
- ROI分析

### エラー対処法
**Excel解析フェーズでの一般的なエラー**:
- **拡張子変更失敗**: ファイル名にスペースや特殊文字が含まれる場合はクォートで囲む
- **zip展開失敗**: ファイルが破損していないか確認、権限チェック
- **XML読み込みエラー**: ファイルエンコーディングの確認
- **シート名文字化け**: 日本語シート名の場合はUTF-8で処理

**Markdown変換フェーズでのエラー**:
- **mermaid構文エラー**: 日本語ラベルの場合は適切にエスケープ
- **表形式の乱れ**: 列数の不整合をチェック
- **ファイル書き込み失敗**: 権限とディスク容量を確認

この指示書に従うことで、Excel解析から最終的なMarkdown変換まで、一貫した品質で作業を実行できます。