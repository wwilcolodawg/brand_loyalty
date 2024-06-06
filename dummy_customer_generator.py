# dummy_customer_generator.py

"""
Module for generating a DataFrame of dummy customer data for a loyalty program.
"""

import pandas as pd
from faker import Faker


class CustomerGenerator:
    """
    A class to generate a DataFrame of dummy customer data for a loyalty program.

    Attributes:
        num_customers (int): Number of dummy customers to generate.
        customers_df (DataFrame): DataFrame containing the generated customer data.
    """

    def __init__(self, num_customers=100):
        """
        Initializes the CustomerGenerator with a specified number of customers.

        Parameters:
            num_customers (int): The number of dummy customer records to generate.
        """
        self.num_customers = num_customers
        self.customers_df = self._generate_customers_df()

    @staticmethod
    def _generate_customer_data(num_customers):
        """
        Generates a list of dictionaries containing fake customer data.

        Parameters:
            num_customers (int): The number of dummy customer records to generate.

        Returns:
            list: A list of dictionaries with customer data.
        """

        """
        Attributes:
            customer_id (str): A unique identifier for the customer.
            first_name (str): The customer's first name.
            last_name (str): The customer's last name.
            email (str): The customer's email address.
            phone (str): The customer's phone number.
            dob (str): The customer's date of birth as a string in YYYY-MM-DD format.
            gender (str): The customer's gender.
            address (str): customer's address
            city (str): customer's city
            state (str): customer's state
            Zip_Code (unknown): customer's zip code
            member_since (str): The date the customer joined the loyalty program.
            newsletter_subscription (bool): Whether the customer is subscribed to the newsletter.
            feedback_provided (bool): Whether the customer has provided feedback.
            communication_preferences (str): The customer's preferred communication channel.
            data_sharing_consent (bool): Whether the customer consents to data sharing.
        """

        fake = Faker()
        customer_data = []
        for _ in range(num_customers):
            customer_dict = {
                "Customer_ID": "CUST" + str(_).zfill(4),
                "First_Name": fake.first_name(),
                "Last_Name": fake.last_name(),
                "Email": fake.email(),
                "Phone": fake.phone_number(),
                "DOB": fake.date_of_birth(minimum_age=18, maximum_age=70).strftime(
                    "%Y-%m-%d"
                ),
                "Gender": fake.random_element(
                    elements=["Male", "Female", "Other", "Prefer not to say"]
                ),
                "Address": fake.street_address(),
                "City": fake.city(),
                "ST": "MN",  # State is set to Minnesota
                "Zip_Code": fake.zipcode_in_state(
                    state_abbr="MN"
                ),  # Zip codes are specific to Minnesota
                "Member_Since": fake.date_between(
                    start_date="-5y", end_date="today"
                ).strftime("%Y-%m-%d"),
                "Newsletter_Subscription": fake.boolean(chance_of_getting_true=75),
                "Feedback_Provided": fake.boolean(chance_of_getting_true=50),
                "Communication_Preferences": fake.random_element(
                    elements=["Email", "SMS", "None"]
                ),
                "Data_Sharing_Consent": fake.boolean(chance_of_getting_true=80),
            }
            customer_data.append(customer_dict)
        return customer_data

    def _generate_customers_df(self):
        """
        Generates a DataFrame of dummy customer data based on the specified number of customers.

        Returns:
            DataFrame: A pandas DataFrame containing the generated customer data.
        """
        customer_data = self._generate_customer_data(self.num_customers)
        return pd.DataFrame(customer_data)
