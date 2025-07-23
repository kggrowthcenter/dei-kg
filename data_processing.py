import streamlit as st
import pandas as pd
from fetch_data import fetch_data_sap, fetch_data_creds

# Fetch the data
@st.cache_data(ttl=86400)
def finalize_data():
    df_sap = fetch_data_sap()
    df_creds = fetch_data_creds()
    # Replace NaN values in the 'layer' column with "N-A" for display and filtering purposes
    df_sap['layer'] = df_sap['layer'].fillna("N-A")
    return df_sap, df_creds