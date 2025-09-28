# Codebase Structure - ExcelAnalyse

## Directory Structure
```
ExcelAnalyse/
├── docs/                                        # Documentation and analysis results
│   ├── AI作業指示書_Excel分析からMarkdown変換.md    # Main workflow instructions
│   ├── result/                                 # AI-generated analysis results (.gitignore target)
│   │   ├── excel_structure_analysis.md        # Excel structure analysis
│   │   ├── [SheetName1]_sheet.md              # Sheet basic analysis
│   │   ├── [SheetName2]_sheet.md              # Sheet basic analysis  
│   │   ├── [SheetName3]_sheet.md              # Sheet basic analysis
│   │   ├── [SheetName1]_詳細.md                # Sheet detailed analysis
│   │   ├── [SheetName2]_詳細.md                # Sheet detailed analysis
│   │   ├── [SheetName3]_詳細フローチャート.md    # Flowchart detailed analysis
│   │   └── [ExcelFileName]_総合分析レポート.md   # Comprehensive analysis report
│   └── サンプル分析結果/                         # Sample analysis results
├── excel_extracted/                            # Extracted Excel files
│   ├── [Content_Types].xml
│   ├── _rels/
│   ├── docProps/
│   └── xl/
│       ├── worksheets/
│       ├── sharedStrings.xml
│       └── workbook.xml
├── [AnyExcelFile].xlsx                         # Target Excel file for analysis
├── [AnyExcelFile].zip                          # ZIP converted file
└── README.md                                   # Project documentation
```

## Key Files
- **AI作業指示書_Excel分析からMarkdown変換.md**: Core workflow instructions with 4 phases
- **README.md**: Project overview and usage documentation
- **経歴書サンプル.xlsx**: Sample Excel file for analysis
- **docs/result/**: Directory for all AI-generated analysis outputs

## File Naming Conventions
- `[シート名]`: Use actual Excel worksheet names as-is
- `[Excelファイル名]`: Use Excel filename without extension
- Support for both Japanese and alphanumeric filenames
- Create `docs/result/` directory if it doesn't exist