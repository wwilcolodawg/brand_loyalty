import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
FOLDER_NAME = "../Data/"
customers_df = pd.read_csv(FOLDER_NAME + "customers.csv")
data = customers_df.copy()


# Sample data loading function (replace with your actual data loading logic)
def load_data():
    # Assuming you have a DataFrame loaded as customers_df
    # For demonstration, creating a DataFrame manually
    data = {"Gender": ["Male", "Female", "Other", "Prefer not to say"]}
    df = pd.DataFrame(data)
    df = pd.concat([df] * 10, ignore_index=True)
    df.loc[5:15, "Gender"] = "Female"
    df.loc[16:25, "Gender"] = "Other"
    df.loc[26:30, "Gender"] = "Prefer not to say"
    return df


# Load your data
customers_df = load_data()

# Count by gender
gender_distribution = customers_df["Gender"].value_counts()

# Set up matplotlib figure
fig, ax = plt.subplots()
ax.pie(
    gender_distribution,
    labels=gender_distribution.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
)
ax.set_title("Customer Gender Distribution")

# Use Streamlit to render the figure
st.pyplot(fig)
