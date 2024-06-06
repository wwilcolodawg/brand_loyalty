# dummy_store_generator.py

"""
Module for generating a DataFrame of dummy store data for a loyalty program.
"""

import pandas as pd
from faker import Faker

fake = Faker()


class StoreGenerator:
    """
    A class to generate a DataFrame of dummy store data for a loyalty program.

    Attributes:
        num_stores (int): Number of dummy stores to generate.
        stores_df (DataFrame): DataFrame containing the generated store data.
    """

    def __init__(self, num_stores=10):
        """
        Initializes the StoreGenerator with a specified number of stores.

        Parameters:
            num_stores (int): The number of dummy store records to generate.
        """
        self.num_stores = num_stores
        self.stores_df = self._generate_stores_df()

    @staticmethod
    def _generate_store_data(num_stores):
        """
        Generates a list of dictionaries containing fake store data.

        Parameters:
            num_stores (int): The number of dummy store records to generate.

        Returns:
            list: A list of dictionaries with store data.
        """
        minnesota_cities = [
            "Minneapolis",
            "St. Paul",
            "Rochester",
            "Duluth",
            "Bloomington",
            "Plymouth",
            "Brooklyn Park",
            "Maple Grove",
            "Woodbury",
            "St. Cloud",
        ]
        store_data = []
        for i in range(num_stores):
            address = fake.street_address()
            city = fake.random_element(elements=minnesota_cities)
            state = "MN"  # Since all cities are in Minnesota
            zipcode = fake.zipcode()
            store_dict = {
                "Store_Name": f"Store_{i+1}",
                "Store_Number": f"STR_{i+1}",
                "Address": address,
                "City": city,
                "State": state,
                "Zip": zipcode,
            }
            store_data.append(store_dict)
        return store_data

    def _generate_stores_df(self):
        """
        Generates a DataFrame of dummy store data based on the specified number of stores.

        Returns:
            DataFrame: A pandas DataFrame containing the generated store data.
        """
        store_data = self._generate_store_data(self.num_stores)
        return pd.DataFrame(store_data)
