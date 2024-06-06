# structure.py
"""
This module establishes the structure of dummy transactions
"""

import pandas as pd

# Specify Data storage folder
FOLDER_NAME = "Data"

# Specify the sheet name or index you want to load
SHEET_NAME = "structure"

# specify the import and export document name
FILE_NAME = "menu"

# Load the specified sheet of the Excel file
structure_df = pd.read_excel(FILE_NAME + ".xlsx", sheet_name=SHEET_NAME)

# saves an saves structure_df as structure.csv
# structure.csv will be used to create a distribution structure for dummy transactions
structure_df.to_csv(FOLDER_NAME + "/" + "structure.csv", index=False)

# creates a csv that determines the probability of different order sizes
# Specify the sheet name or index you want to load
SHEET_NAME = "order_size"

# Load the specified sheet of the Excel file
order_size_df = pd.read_excel(FILE_NAME + ".xlsx", sheet_name=SHEET_NAME)

# saves an saves order_size_df as order_size.csv
# structure.csv will be used to create a distribution structure for dummy transactions
order_size_df.to_csv(FOLDER_NAME + "/" + "order_size.csv", index=False)
