
import pandas as pd
from sklearn.preprocessing import StandardScaler

def feature_engineering(input_file, output_file):
    df = pd.read_csv(input_file)
    scaler = StandardScaler()
    df[['feature1', 'feature2']] = scaler.fit_transform(df[['feature1', 'feature2']])
    df.to_csv(output_file, index=False)
    print("Features engineered and saved.")

if __name__ == "__main__":
    feature_engineering("data/processed/cleaned_data.csv", "data/processed/engineered_data.csv")
