import streamlit as st

# Create a form
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=100, value=0)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Hello {name}, you are {age} years old.")
