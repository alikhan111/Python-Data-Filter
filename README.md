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


Or clone the repository:

bash
git clone https://github.com/yourusername/csv-filter.git
cd csv-filter
Usage
Place all CSV files you want to filter in the same directory as the script

Run the script:

bash
python filter_data.py
Follow the prompts to enter filter values for each column

Leave fields blank if you don't want to filter on that column

At least one column filter must be specified

The script will output:

Total number of rows scanned

Number of matching rows found

Location of the output file (if matches were found)

Example
bash
$ python filter_data.py
Please enter filter values:
Leave fields blank if not applicable:
Column Entry 1: USA
Column Entry 2: California
Column Entry 3: 
Column Entry 4: 
Column Entry 5: 
Column Entry 6: 
Data Crunching...
Processing Files...
Analysing Data...
Task Complete!
Scanned Entries: 1250.
Match Entries: 42.
File Created: new_file.csv
This would find all rows where:

Column 1 equals "USA" AND

Column 2 equals "California"

Output
The filtered results are saved to new_file.csv in the same directory, containing:

The original header row from the input files

All rows that match the specified filters

Notes
The script assumes all input CSV files have the same structure/headers

Only exact matches are supported (case-sensitive)

The first row of the first CSV file is treated as the header

Temporary files are automatically removed when done

License
MIT License

text

This README includes all the essential information users would need to understand and use your script. You may want to:

1. Adjust the download URLs if you host this in a specific repository
2. Add a license file if you choose a specific license
3. Include more detailed examples if your script has advanced features
4. Add a "Contributing" section if you want others to help develop it

The README is written in Markdown format and will render nicely on GitHub or other platforms that support Markdown.
