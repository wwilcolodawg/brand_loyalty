# menu_import.py
"""
This module imports the working menu.xlsx file and converts it to menu.csv
"""

import pandas as pd

# Specify Data storage folder
FOLDER_NAME = "Data"

# Specify the sheet name or index you want to load
SHEET_NAME = "export"

# specify the import and export document name
FILE_NAME = "menu"

# Load the specified sheet of the Excel file
excel_data = pd.read_excel(FILE_NAME + ".xlsx", sheet_name=SHEET_NAME)

# Save as a CSV file
excel_data.to_csv(FOLDER_NAME + "/" + FILE_NAME + ".csv", index=False)


# Import menu.csv
menu_df = pd.read_csv(FOLDER_NAME + "/" + FILE_NAME + ".csv")

# declare groups of menu items that need to be analyzed
groups_list = ["Primary", "Beverage"]

# Filter for 'Primary' group
analysis_df = menu_df[menu_df["Group"].isin(groups_list)].copy()


# saves an analysis_menu.csv for data analysis
analysis_df.to_csv(FOLDER_NAME + "/" + FILE_NAME + "_analysis.csv", index=False)
