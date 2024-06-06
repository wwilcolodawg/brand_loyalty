import pandas as pd
from faker import Faker
import random

fake = Faker()

# Define your probabilities and distributions here
# Assuming item probability matrices are defined as dictionaries like those shown above
entree_probs = {1: 0.10, 2: 0.15}
beverage_probs = {1: 0.20, 2: 0.25}


def generate_dummy_transactions(num_transactions):
    transactions = []

    for _ in range(num_transactions):
        order_number = fake.unique.random_int(min=1000, max=9999)
        transaction_date = fake.date_between(
            start_date="-1y", end_date="today"
        ).strftime("%Y-%m-%d")
        transaction_time = fake.time()

        # Assuming 'entree_probs' and 'beverage_probs' are already defined dictionaries
        entree_choice = "E_" + str(
            random.choices(list(entree_probs.keys()), weights=entree_probs.values())[0]
        )
        beverage_choice = "B_" + str(
            random.choices(
                list(beverage_probs.keys()), weights=beverage_probs.values()
            )[0]
        )

        # Add separate rows for entree and beverage if both are ordered
        transactions.append(
            [order_number, transaction_date, transaction_time, entree_choice]
        )

        # Some logic to determine if a beverage should be ordered
        if random.random() <= probability_of_ordering_beverage:
            transactions.append(
                [order_number, transaction_date, transaction_time, beverage_choice]
            )

        # Additional logic for group orders can be included here

    transaction_df = pd.DataFrame(
        transactions,
        columns=["Order_number", "Transaction_date", "Transaction_time", "Order_item"],
    )
    return transaction_df


# Define the probability of ordering a beverage
probability_of_ordering_beverage = 0.75  # as an example

# Assuming 'entree_probs' and 'beverage_probs' dictionaries are already defined
# and contain the menu items probabilities

# Generate the transactions
dummy_transactions_df = generate_dummy_transactions(100)

# Convert to DataFrame and save as CSV, if needed
dummy_transactions_df.to_csv("dummy_transactions.csv", index=False)
