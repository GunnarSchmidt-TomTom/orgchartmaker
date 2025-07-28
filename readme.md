# Org Chart Maker

A powerful Python command-line tool that generates organizational charts from employee data. Supports multiple input formats and output styles for flexible org chart visualization.

## Features

- **Multiple Input Formats**: CSV (semicolon-delimited) and Excel files (.xlsx, .xls)
- **Flexible Output Options**: ASCII trees, PNG images (GraphViz), or CSV statistics
- **Advanced Filtering**: Show only managers, focus on specific manager subtrees
- **Performance Optimized**: Handles large datasets efficiently with binary search algorithms
- **Robust Error Handling**: Graceful handling of malformed data with detailed error messages

## Quick Start

### Installation

```bash
# Install required dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Generate PNG org chart (default)
python3 orgchart.py --input data.csv

# Generate ASCII tree view
python3 orgchart.py --input employees.xlsx --ascii

# Generate team size statistics
python3 orgchart.py --input data.csv --orgsize

# Show only managers
python3 orgchart.py --input data.xlsx --only-managers

# Focus on specific manager's organization
python3 orgchart.py --input data.csv --root "John Smith" --ascii
```

## Input Formats

### CSV Format
Semicolon-delimited files (like Workday exports):
```
Unique Identifier;Name;Reports To;Line Detail 1;Line Detail 2;Organization Name
emp001;John Smith;;Director of Engineering;;
emp002;Jane Doe;emp001;Senior Manager;;
```

### Excel Format
Excel files (.xlsx or .xls) with columns:
- **Column A**: Unique Identifier (Employee ID)
- **Column B**: Name (Full Name)
- **Column C**: Reports To (Manager's Employee ID)  
- **Column D**: Line Detail 1 (Job Title)

*Additional columns are ignored, making it compatible with standard Workday exports.*

## Output Options

### ASCII Tree (`--ascii`)
Terminal-friendly hierarchical display:
```
John Smith (Director of Engineering) -- 25
├── Jane Doe (Senior Manager) -- 12
│   ├── Bob Wilson (Engineer)
│   └── Alice Brown (Engineer)
└── Mike Johnson (Senior Manager) -- 11
    └── Sarah Davis (Engineer)
```

### PNG Image (default)
High-quality organizational chart using GraphViz:
- Visual boxes with names and titles
- Clear reporting lines
- Automatic layout optimization
- Outputs to `out.png` by default

### Statistics CSV (`--orgsize`)
Management metrics in CSV format:
```
manager;title;total org size;number of directs
John Smith;Director of Engineering;25;2
Jane Doe;Senior Manager;12;2
```

## Advanced Options

- `--only-managers`: Display only employees with direct reports
- `--root "Name"`: Show organizational subtree for specific manager
- `--help`: Display all available options

## Requirements

- **Python 3.6+**
- **pydot**: PNG image generation (requires GraphViz installation)
- **treelib**: ASCII tree rendering
- **openpyxl**: Excel file support

## Dependencies Installation

```bash
# Install GraphViz (system dependency)
# macOS: brew install graphviz
# Ubuntu: sudo apt-get install graphviz
# Windows: Download from graphviz.org

# Install Python packages
pip install pydot treelib openpyxl
```

## Examples

```bash
# View all options
python3 orgchart.py --help

# Process Workday export
python3 orgchart.py --input workday_export.xlsx --ascii

# Generate management-only view
python3 orgchart.py --input team_data.csv --only-managers

# Focus on engineering org
python3 orgchart.py --input company.xlsx --root "VP Engineering" --ascii

# Export team statistics  
python3 orgchart.py --input data.csv --orgsize > team_stats.csv
```

## Error Handling

The tool provides comprehensive error handling for:
- Missing or invalid input files
- Malformed CSV/Excel data
- Insufficient column data
- Circular reporting relationships
- Missing GraphViz dependencies

## Performance

Optimized for large organizations:
- Efficient CSV parsing with proper encoding support
- Binary search algorithms for employee lookups
- Memory-efficient data structures
- Handles thousands of employees seamlessly