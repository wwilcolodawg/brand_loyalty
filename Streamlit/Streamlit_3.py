import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Set up directory paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Data")


def load_data():
    menu_df = pd.read_csv(os.path.join(DATA_DIR, "menu_analysis.csv"))
    customers_df = pd.read_csv(os.path.join(DATA_DIR, "customers.csv"))
    stores_df = pd.read_csv(os.path.join(DATA_DIR, "stores.csv"))
    transactions_df = pd.read_csv(
        os.path.join(DATA_DIR, "transactions.csv"), parse_dates=["Transaction_Date"]
    )
    return menu_df, customers_df, stores_df, transactions_df


menu_df, customers_df, stores_df, transactions_df = load_data()

# Data Management
transactions_with_prices = pd.merge(
    transactions_df,
    menu_df[["Item_Number", "Price"]],  # Select only necessary columns from menu_df
    on="Item_Number",
    how="left",
)

# Streamlit UI
st.title("Quick Service Curry Restaurant Chain Dashboard")

# Display total sales by store
st.header("Sales Performance by Store")
store_sales = (
    transactions_with_prices.groupby("Store_Number")["Price"].sum().reset_index()
)
fig, ax = plt.subplots()
ax.bar(store_sales["Store_Number"], store_sales["Price"], color="lightblue")
ax.set_xlabel("Store Number")
ax.set_ylabel("Total Sales")
ax.set_title("Total Sales by Store")
st.pyplot(fig)

# Display customer demographics
st.header("Customer Demographics")
gender_counts = customers_df["Gender"].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
ax1.set_title("Customer Gender Distribution")
st.pyplot(fig1)

# Adding filters
store_filter = st.sidebar.multiselect(
    "Select Store", stores_df["Store_Number"].unique()
)

# Ensure that the dates are properly formatted for the slider
min_date = transactions_df["Transaction_Date"].min().date()
max_date = transactions_df["Transaction_Date"].max().date()

# Slider for date filtering
date_filter = st.sidebar.date_input(
    "Select Date Range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date,
)

# Filter data based on selections
if store_filter:
    transactions_df = transactions_df[
        transactions_df["Store_Number"].isin(store_filter)
    ]

# Display menu item performance
st.header("Menu Item Performance")
item_sales = (
    transactions_with_prices.groupby("Item_Number")["Price"].sum().reset_index()
)
fig2, ax2 = plt.subplots()
ax2.bar(item_sales["Item_Number"], item_sales["Price"], color="green")
ax2.set_xlabel("Item Number")
ax2.set_ylabel("Total Sales")
ax2.set_title("Sales by Menu Item")
st.pyplot(fig2)
