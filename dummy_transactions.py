# dummy_transactions.py
"""
Module for generating a DataFrame of dummy customer transactions at stores
"""

import random
import pandas as pd
from faker import Faker

# Specify Data storage folder
FOLDER_NAME = "Data"

# Initialize Faker
fake = Faker()

# Load data from CSV files
menu_df = pd.read_csv(FOLDER_NAME + "/" + "menu_analysis.csv")
customers_data_df = pd.read_csv(FOLDER_NAME + "/" + "customers.csv")
stores_data_df = pd.read_csv(FOLDER_NAME + "/" + "stores.csv")
structure_data_df = pd.read_csv(FOLDER_NAME + "/" + "structure.csv")
size_data_df = pd.read_csv(FOLDER_NAME + "/" + "order_size.csv")


def generate_dummy_transactions(
    # function fore creating dummy tractions utilizing directing csv(s)
    structure_df,
    customers_df,
    stores_df,
    size_df,
    num_transactions,
):
    transactions = []

    # Normalize the Order_Size_Prob if not summing to 1
    size_df["Order_Size_Prob"] = (
        size_df["Order_Size_Prob"] / size_df["Order_Size_Prob"].sum()
    )
    order_sizes = size_df["Order_size"].tolist()
    size_probabilities = size_df["Order_Size_Prob"].tolist()

    for _ in range(num_transactions):
        order_number = fake.unique.random_int(min=1000, max=150_000)
        transaction_date = fake.date_between(
            start_date="-1y", end_date="today"
        ).strftime("%Y-%m-%d")
        transaction_time = fake.time()
        store_number = random.choice(stores_df["Store_Number"])
        customer_id = random.choice(customers_df["Customer_ID"])

        # Determine the number of items in this transaction
        num_items = random.choices(order_sizes, weights=size_probabilities, k=1)[0]

        for _ in range(num_items):
            item_choice = random.choices(
                population=structure_df["Item_Num"],
                weights=structure_df["Order_Prob"],
                k=1,
            )[0]

            transactions.append(
                {
                    "Order_Number": order_number,
                    "Transaction_Date": transaction_date,
                    "Transaction_Time": transaction_time,
                    "Store_Number": store_number,
                    "Customer_ID": customer_id,
                    "Item_Number": item_choice,
                }
            )

    return pd.DataFrame(transactions)


# Generate the transactions
NUM_DUMMY_TRANSACTIONS = (
    100_000  # Specify the number of transactions you want to generate
)
dummy_transactions_df = generate_dummy_transactions(
    structure_data_df,
    customers_data_df,
    stores_data_df,
    size_data_df,
    NUM_DUMMY_TRANSACTIONS,
)

# Save the generated transactions to a CSV file
dummy_transactions_df.to_csv(FOLDER_NAME + "/" + "transactions.csv", index=False)
