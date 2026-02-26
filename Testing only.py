import os
import pandas as pd
import logging
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from utils import standardize_date, validate_schema

def extract():
    all_files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith(".csv")]
    df_list = []








