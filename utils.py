# utils.py (Reusable Components)
import  logging as l
from datetime import datetime

def setup_logger(log_file1):
            l.basicConfig(
            filename=log_file1,
            level=l.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
def standardize_date(date_value):
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(str(date_value), fmt).date()
        except ValueError:
            continue
    return None

def validate_schema(df):
    required_c = ["order_id","customer_id","order_date","amount","city"]
    return all(col in df.columns for col in required_c)
