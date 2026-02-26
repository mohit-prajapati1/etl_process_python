import os
import pandas as pd
import logging as l
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from utils import standardize_date, validate_schema

def extract():
    all_files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith(".csv")]
    df_list = []

    for file in all_files:
        df = pd.read_csv(RAW_DATA_PATH + file)
        df_list.append(df)
        l.info(f"Extracted file: {file}")
    return pd.concat(df_list, ignore_index=True)

def transform(df):
    if not validate_schema(df):
        l.error("Schema validation failed")
        raise Exception("Invalid schema")

    # Remove duplicates
    df = df.drop_duplicates().copy()

    # Standardize date
    df["order_date"] = df["order_date"].apply(standardize_date)

    # Convert amount to numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Handle missing amount
    df["amount"] = df["amount"].fillna(0)

    return df
def load(df):
    df.to_csv(PROCESSED_DATA_PATH + "clean_sales.csv", index=False)

    summary = df.groupby("city")["amount"].sum().reset_index()
    summary.to_csv(PROCESSED_DATA_PATH + "sales_summary.csv", index=False)

    l.info("Data loaded successfully")
