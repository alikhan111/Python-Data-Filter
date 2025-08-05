#!/usr/bin/env python3

import os
import sys
from typing import List, Optional

### File Names ###
NEW_FILE = 'new_file.csv'
MERGE_FILE = 'temp_file'

### User Input Data ###
user_level1: Optional[str] = None
user_level2: Optional[str] = None
user_level3: Optional[str] = None
user_level4: Optional[str] = None
user_level5: Optional[str] = None
user_level6: Optional[str] = None

### System Input Data ###
level1: str
level2: str
level3: str
level4: str
level5: str
level6: str

### Important Variables ###
full_data: List[str] = []
new_data: List[str] = []
num: int = 0
total_num: int = 0

def collect_user_data() -> None:
    """Collect user input data for filtering"""
    global user_level1, user_level2, user_level3, user_level4, user_level5, user_level6
    
    print("Please enter filter values:")
    print("Leave fields blank if not applicable:")
    
    user_level1 = input("Column Entry 1: ").strip()
    if not user_level1:
        user_level1 = None
        
    user_level2 = input("Column Entry 2: ").strip()
    if not user_level2:
        user_level2 = None
        
    user_level3 = input("Column Entry 3: ").strip()
    if not user_level3:
        user_level3 = None
        
    user_level4 = input("Column Entry 4: ").strip()
    if not user_level4:
        user_level4 = None
        
    user_level5 = input("Column Entry 5: ").strip()
    if not user_level5:
        user_level5 = None
        
    user_level6 = input("Column Entry 6: ").strip()
    if not user_level6:
        user_level6 = None
    
    # Check if all variables are undefined
    if all(v is None for v in [user_level1, user_level2, user_level3, 
                              user_level4, user_level5, user_level6]):
        print("Nothing Is Defined.")
        print("Processed Stopped.")
        sys.exit()

def create_merge_file() -> None:
    """Create a merged file from all CSV files in the directory"""
    print("Data Crunching...")
    print("Processing Files...")
    
    # Delete old merge file if exists
    if os.path.exists(MERGE_FILE):
        os.unlink(MERGE_FILE)
    if os.path.exists(NEW_FILE):
        os.unlink(NEW_FILE)
    
    # Create new merge file
    if os.name == 'nt':  # Windows
        os.system(f'type *.csv > {MERGE_FILE}')
    else:  # Unix-like
        os.system(f'cat *.csv > {MERGE_FILE}')
    
    # Convert line endings (simplified approach)
    if os.path.exists(MERGE_FILE):
        with open(MERGE_FILE, 'r', newline='') as f:
            content = f.read()
        with open(MERGE_FILE, 'w', newline='\r\n') as f:
            f.write(content)

def read_merge_file() -> None:
    """Read the merged file into memory"""
    global full_data
    try:
        with open(MERGE_FILE, 'r') as f:
            full_data = f.readlines()
    except IOError as e:
        print(f"Cannot open file: {e}")
        sys.exit(1)

def filter_data(value: str) -> bool:
    """Filter data based on user input"""
    global level1, level2, level3, level4, level5, level6, num
    
    value = value.lstrip()
    values = value.strip().split(',')
    
    # Ensure we have at least 6 columns, pad with empty strings if needed
    values.extend([''] * (6 - len(values)))
    level1, level2, level3, level4, level5, level6 = values[:6]
    
    # Check all possible combinations of user-defined levels
    conditions = []
    
    if user_level1 is not None:
        conditions.append(level1 == user_level1)
    if user_level2 is not None:
        conditions.append(level2 == user_level2)
    if user_level3 is not None:
        conditions.append(level3 == user_level3)
    if user_level4 is not None:
        conditions.append(level4 == user_level4)
    if user_level5 is not None:
        conditions.append(level5 == user_level5)
    if user_level6 is not None:
        conditions.append(level6 == user_level6)
    
    # If all conditions are met (for defined levels)
    if all(conditions):
        new_data.append(value)
        num += 1
        return True
    return False

def analyse_data() -> None:
    """Analyze the data and apply filters"""
    global total_num
    print("Analysing Data...")
    
    for val in full_data:
        total_num += 1
        filter_data(val)

def save_new_file() -> None:
    """Save the filtered data to a new file"""
    if not new_data:
        print("Zero Match.")
        remove_merge_file()
        sys.exit()
    
    try:
        with open(NEW_FILE, 'w') as f:
            if full_data:
                f.write(full_data[0])  # Write headers
            f.writelines(new_data)
    except IOError as e:
        print(f"Cannot save file: {e}")
        sys.exit(1)

def remove_merge_file() -> None:
    """Remove the temporary merge file"""
    if os.path.exists(MERGE_FILE):
        os.unlink(MERGE_FILE)

def main() -> None:
    """Main function"""
    collect_user_data()
    create_merge_file()
    read_merge_file()
    analyse_data()
    save_new_file()
    remove_merge_file()
    
    print("Task Complete!")
    print(f"Scanned Entries: {total_num}.")
    print(f"Match Entries: {num}.")
    
    if num > 0:
        print(f"File Created: {NEW_FILE}")

if __name__ == "__main__":
    main()
