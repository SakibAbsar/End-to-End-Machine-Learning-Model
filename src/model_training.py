
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def train_model():
    config = load_config()
    df = pd.read_csv("data/processed/engineered_data.csv")
    X = df.drop(columns=["target"])
    y = df["target"]
    
    model = RandomForestClassifier(**config["model"]["parameters"])
    model.fit(X, y)

    with open(config["data"]["model_save_path"], "wb") as f:
        pickle.dump(model, f)
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()
