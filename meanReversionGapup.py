import pandas as pd
import numpy as np
from pymongo import MongoClient
import matplotlib.pyplot as plt
import streamlit as st

# Title of the app
st.title("Gap-Up Strategy Analysis")

# Subheader with additional description
st.subheader("Analyzing Cumulative PNL from Gap-Up Trading Strategy")

# Sidebar for user inputs (optional)
st.sidebar.header("Settings")
refresh_button = st.sidebar.button("Refresh Data")

# Connect to MongoDB
mongo = MongoClient("mongodb+srv://my_algo_user:aUdNEfbaM2MDd3k8@cluster0.otr8r.mongodb.net/?retryWrites=true&w=majority")
mydb = mongo['Test1']
coll = mydb["Pnl_Gap"]

# Function to fetch and process data
@st.cache(ttl=600)  # Use @st.cache instead of @st.cache_data
def load_data():
    # Fetch data from MongoDB
    table = list(coll.find({}, {'_id': 0, 'Date': 1, 'PNL': 1}))
    # Convert data to DataFrame
    df = pd.DataFrame(table)
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date is in datetime format
    df['Cumulative PNL'] = df['PNL'].cumsum()
    return df

# Load data (with caching)
if refresh_button:
    st.cache.clear()  # Use st.cache.clear() to clear the cache

data = load_data()

# Display the DataFrame
st.write("### PNL Data Table", data)

# Plot the cumulative PNL
st.write("### Cumulative PNL Over Time")
st.line_chart(data.set_index('Date')['Cumulative PNL'])

# Display the total PNL
total_pnl = data['Cumulative PNL'].iloc[-1]
st.write(f"### Total Cumulative PNL: {total_pnl}")

# Additional insights (Optional)
average_pnl = data['PNL'].mean()
max_pnl = data['PNL'].max()
min_pnl = data['PNL'].min()

st.write("### Additional Insights")
st.write(f"- Average Daily PNL: {average_pnl}")
st.write(f"- Maximum Single-Day PNL: {max_pnl}")
st.write(f"- Minimum Single-Day PNL: {min_pnl}")
