"""
This module generates dummy transactions by utilizing dummy data from the customers,stores,
 and menu tables
"""

import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Assuming menu_df, customers_df, and stores_df are already loaded as described
# For demonstration, these should be replaced with the actual loaded DataFrames


# Generate dummy transactions
def generate_transactions(menu_df, customers_df, stores_df, num_transactions=100):
    transactions = []

    for i in range(num_transactions):
        # Randomly choose a customer, store, and number of items
        customer_id = random.choice(customers_df["Customer_ID"])
        store_number = random.choice(stores_df["Store_Number"])
        num_items = random.randint(
            1, 4
        )  # Assuming 1 to 4 items per transaction for variability

        # Transaction date and time
        transaction_date = fake.date_between(start_date="-2y", end_date="today")
        transaction_time = fake.time()

        # Generate individual item entries
        for _ in range(num_items):
            item_number = random.choice(menu_df["Item_Num"])
            transactions.append(
                [
                    f"TRANS{i+1}",
                    transaction_date,
                    transaction_time,
                    store_number,
                    customer_id,
                    item_number,
                ]
            )

    # Convert to DataFrame
    transactions_df = pd.DataFrame(
        transactions,
        columns=[
            "Order_number",
            "Transaction_date",
            "Transaction_time",
            "Store_number",
            "Customer_ID",
            "Item_number",
        ],
    )

    return transactions_df


# Import supporting input data frames menu, customers, and stores
MENU_CSV = "menu_analysis.csv"
CUSTOMERS_CSV = "customers.csv"
STORES_CSV = "stores.csv"

menu_df = pd.read_csv(MENU_CSV)
customers_df = pd.read_csv(CUSTOMERS_CSV)
stores_df = pd.read_csv(STORES_CSV)

# Generate dummy transactions DataFrame
dummy_transactions_df = generate_transactions(menu_df, customers_df, stores_df)

# Display the first few rows of the generated DataFrame
print(dummy_transactions_df.head())
dummy_transactions_df.to_csv("transactions.csv", index=False)
