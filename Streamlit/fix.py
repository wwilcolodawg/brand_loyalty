import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set up directory paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Data")

menu_df = pd.read_csv(os.path.join(DATA_DIR, "menu_analysis.csv"))
customers_df = pd.read_csv(os.path.join(DATA_DIR, "customers.csv"))
stores_df = pd.read_csv(os.path.join(DATA_DIR, "stores.csv"))
transactions_df = pd.read_csv(os.path.join(DATA_DIR, "transactions.csv"))

# store_sales = transactions_df.groupby("Store_Number")["Price"].sum().reset_index()
print(transactions_df[""])
