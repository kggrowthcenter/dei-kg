import streamlit as st
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread

@st.cache_resource(ttl=86400)
def get_gspread_client(secret_key: str):
    secret_info = st.secrets[secret_key]
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(secret_info, scope)
    return gspread.authorize(creds)

@st.cache_data(ttl=86400)
def fetch_data_sap():
    client = get_gspread_client("json_sap")
    spreadsheet = client.open("0. Active Employee - Monthly Updated")
    sheet = spreadsheet.sheet1

    data = sheet.get_all_records()
    df_sap = pd.DataFrame(data)
    return df_sap

@st.cache_data(ttl=86400)
def fetch_data_creds():
    client = get_gspread_client("json_sap")
    spreadsheet = client.open("Discovery Test Result - Dashboard Credentials")
    sheet = spreadsheet.sheet1

    data = sheet.get_all_records()
    df_creds = pd.DataFrame(data)
    return df_creds