# data_utils.py
import pandas as pd
import streamlit as st

def load_data(file):
    """
    Attempts to read an Excel or CSV file and return a DataFrame.
    """
    try:
        if isinstance(file, str):
            # local path
            if file.endswith(".xlsx"):
                return pd.read_excel(file)
            elif file.endswith(".csv"):
                return pd.read_csv(file)
            else:
                return None
        else:
            # user-uploaded file
            if file.name.endswith(".xlsx"):
                return pd.read_excel(file)
            elif file.name.endswith(".csv"):
                return pd.read_csv(file)
            else:
                return None
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None
