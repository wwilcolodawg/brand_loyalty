import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Load data from CSV files
menu_df = pd.read_csv("menu_analysis.csv")
customers_df = pd.read_csv("customers.csv")
stores_df = pd.read_csv("stores.csv")
structure_df = pd.read_csv("structure.csv")


def generate_dummy_transactions(
    structure_df, customers_df, stores_df, num_transactions
):
    transactions = []
    store_numbers = stores_df[
        "Store_Number"
    ].tolist()  # Get the list of store numbers from the stores_df

    for _ in range(num_transactions):
        order_number = fake.unique.random_int(min=1000, max=9999)
        transaction_date = fake.date_between(
            start_date="-1y", end_date="today"
        ).strftime("%Y-%m-%d")
        transaction_time = fake.time()
        store_number = random.choice(store_numbers)  # Choose from actual store numbers
        customer_id = random.choice(customers_df["Customer_ID"])

        item_choice = random.choices(
            population=structure_df["Item_Num"], weights=structure_df["Order_Prob"], k=1
        )[0]

        transactions.append(
            {
                "Order_number": order_number,
                "Transaction_date": transaction_date,
                "Transaction_time": transaction_time,
                "Store_number": store_number,  # Use the actual store number
                "Customer_ID": customer_id,
                "Item_number": item_choice,
            }
        )

    return pd.DataFrame(transactions)


# Generate the transactions
num_dummy_transactions = 100
dummy_transactions_df = generate_dummy_transactions(
    structure_df, customers_df, stores_df, num_dummy_transactions
)

# Save the generated transactions to a CSV file
dummy_transactions_df.to_csv("transactions.csv", index=False)
