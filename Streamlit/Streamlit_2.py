import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set up the directory structure
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)  # Directory where the script is located
DATA_DIR = os.path.join(
    BASE_DIR, "Data"
)  # Adjusted to directly use 'Data' within the same folder level


# Function to load data files dynamically
def load_data(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    return pd.read_csv(file_path)


def plot_sales(transactions_df, menu_df):
    # Merge transactions with menu details
    transaction_details = transactions_df.merge(
        menu_df, left_on="Item_Number", right_on="Item_Number"
    )

    # Calculate sales per item
    sales_per_item = (
        transaction_details.groupby("Ingredient").agg({"Price": "sum"}).reset_index()
    )

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(sales_per_item["Ingredient"], sales_per_item["Price"], color="skyblue")
    plt.xlabel("Menu Item")
    plt.ylabel("Total Sales ($)")
    plt.title("Sales Performance by Menu Item")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt


def main():
    st.title("Sales Performance Dashboard")

    # Load data using dynamic paths
    transactions_df = load_data("transactions.csv")
    menu_df = load_data("menu.csv")

    # Button to trigger the plot display
    if st.button("Show Plot"):
        fig = plot_sales(transactions_df, menu_df)
        st.pyplot(fig)


if __name__ == "__main__":
    main()
