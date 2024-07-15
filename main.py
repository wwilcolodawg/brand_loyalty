# main.py

from dummy_customer_generator import CustomerGenerator
from dummy_store_generator import StoreGenerator

# Specify Data storage folder
FOLDER_NAME = "Data"

# Initialize the CustomerGenerator with a specific number of dummy customers
NUM_CUSTOMERS = 10_000
customer_generator = CustomerGenerator(NUM_CUSTOMERS)

# Initialize the StoreGenerator with a specific number of dummy stores
NUM_STORES = 10
store_generator = StoreGenerator(NUM_STORES)

# Access the generated DataFrames
customers_df = customer_generator.customers_df
stores_df = store_generator.stores_df

# Save to CSV
customers_df.to_csv(FOLDER_NAME + "/" + "customers.csv", index=False)
stores_df.to_csv(FOLDER_NAME + "/" + "stores.csv", index=False)

# Future project move all other. py files to load here, so I only have to run main.py
