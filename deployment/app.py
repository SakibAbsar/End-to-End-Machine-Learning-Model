
from flask import Flask, request, jsonify
import pickle
import yaml
import pandas as pd

app = Flask(__name__)

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

with open(config["data"]["model_save_path"], "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
