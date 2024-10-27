
import pandas as pd
import os
import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def preprocess_data(file_path):
    config = load_config()
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)  # Simple missing value handling
    df.to_csv(config["data"]["processed_data_path"] + "cleaned_data.csv", index=False)
    print("Data preprocessed and saved.")

if __name__ == "__main__":
    preprocess_data("data/raw/sample_data.csv")
