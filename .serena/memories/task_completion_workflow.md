# Task Completion Workflow - ExcelAnalyse

## When a Task is Completed

Since ExcelAnalyse is primarily a documentation/analysis project, task completion involves:

### 1. Analysis Workflow Completion
Follow the 4-phase process defined in `docs/AI作業指示書_Excel分析からMarkdown変換.md`:
- **Phase 0**: Excel analysis and extraction
- **Phase 1+**: Markdown conversion and analysis  
- **Phase 4**: Quality verification and comparison check

### 2. File Organization Check
- Ensure all AI-generated files are in `docs/result/` directory
- Verify proper file naming conventions are followed
- Check that all required analysis documents are created

### 3. Quality Verification (Phase 4)
- Compare generated Markdown against original Excel file
- Check for data omissions or misrepresentations
- Verify accuracy of:
  - String data completeness
  - Numerical data accuracy
  - Structural relationships
  - Expression appropriateness

### 4. Documentation Updates
- Update project documentation if new patterns are discovered
- Ensure README.md reflects current capabilities
- Update instruction manual if workflow improvements are identified

## No Traditional Development Commands
- **No linting**: No code linting tools present
- **No testing**: No test frameworks available
- **No building**: No build processes required
- **No formatting**: Content formatting handled through Markdown standards

## Git Operations (Optional)
- Review changes with `git status` and `git diff`
- Commit completed analysis work if requested
- Use descriptive commit messages for documentation changes