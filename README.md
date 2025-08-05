# CSV Data Filtering Tool

A Python script that filters data from multiple CSV files based on user-specified column values.

## Description

This tool merges all CSV files in the current directory and allows filtering rows based on exact matches in up to 6 columns. The filtered results are saved to a new CSV file while preserving the original headers.

## Features

- Merges all CSV files in the current directory
- Filters data based on exact matches in 1-6 columns
- Preserves original headers in output
- Handles empty/undefined filter values
- Provides statistics on scanned and matched entries
- Cleans up temporary files automatically

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library modules)

## Installation

No installation required. Simply download the script:

```bash
wget https://raw.githubusercontent.com/yourusername/csv-filter/main/filter_data.py
