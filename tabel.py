import streamlit as st
import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame as a table
st.table(df)
