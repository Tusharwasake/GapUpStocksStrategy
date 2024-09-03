import pandas as pd 
import numpy as np
from pymongo import MongoClient
import matplotlib.pyplot as plt
import streamlit as st

# Title of the app
st.title("Gapup Strategy")

# Connect to MongoDB
mongo = MongoClient("mongodb+srv://my_algo_user:aUdNEfbaM2MDd3k8@cluster0.otr8r.mongodb.net/?retryWrites=true&w=majority")
mydb = mongo['Test1']
coll = mydb["Pnl_Gap"]

# Fetch data from MongoDB
table = list(coll.find(
    {}, {'_id': 0, 'Date': 1, 'PNL': 1}))

# Extract dates and PNLs
date = [item['Date'] for item in table]
pnl = [item['PNL'] for item in table]

# Calculate cumulative PNL
Sum_pnl = np.cumsum(pnl)

# Create a DataFrame for the chart
chart_data = pd.DataFrame({
    'Date': date,
    'Cumulative PNL': Sum_pnl
})

# Set the date as the index for better plotting
chart_data.set_index('Date', inplace=True)

# Plot the cumulative PNL
st.line_chart(chart_data)

# Display the table of data
st.table(table)

# Display the total PNL
st.write("### Total PNL: ", Sum_pnl[-1])
