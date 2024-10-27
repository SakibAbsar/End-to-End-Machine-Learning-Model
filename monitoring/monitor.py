
import requests
import time

def monitor_predictions():
    url = "http://localhost:5000/predict"
    while True:
        data = {"feature1": 1.2, "feature2": 0.4}  # Example data
        response = requests.post(url, json=data)
        print(f"Prediction: {response.json()}")
        time.sleep(60)  # Run every minute

if __name__ == "__main__":
    monitor_predictions()
