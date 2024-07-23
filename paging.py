import streamlit as st

# Function to display pages
def page_1():
    st.write("This is Page 1")

def page_2():
    st.write("This is Page 2")

def page_3():
    st.write("This is Page 3")

# Dictionary of pages
pages = {
    "Page 1": page_1,
    "Page 2": page_2,
    "Page 3": page_3
}

# Sidebar for page selection
page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Display the selected page
pages[page]()
