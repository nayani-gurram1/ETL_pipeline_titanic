# extract.py
# ===========================
# Purpose: Extract Telco Customer Churn dataset
# ===========================

import os
import pandas as pd
import opendatasets as od

def extract_data():
    # Project root
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data", "raw")
    os.makedirs(data_dir, exist_ok=True)

    # Download dataset from Kaggle
    dataset_url = "https://www.kaggle.com/datasets/blastchar/telco-customer-churn"
    od.download(dataset_url, data_dir=data_dir)

    # Find CSV file in downloaded folder
    raw_folder = os.path.join(data_dir, "telco-customer-churn")
    raw_csv = [f for f in os.listdir(raw_folder) if f.endswith(".csv")][0]

    # Load and save standardized raw CSV
    df = pd.read_csv(os.path.join(raw_folder, raw_csv))
    raw_path = os.path.join(data_dir, "churn_raw.csv")
    df.to_csv(raw_path, index=False)

    print(f"✅ Data extracted and saved at: {raw_path}")
    return raw_path

if __name__ == "__main__":
    extract_data()
