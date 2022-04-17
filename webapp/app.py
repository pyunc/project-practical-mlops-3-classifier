from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

def scale(payload):
    scaler = StandardScaler().fit(payload)
    return scaler.transform(payload)

@app.route('/', methods=['GET'])
def home():
    return "<h3>Sklearn Prediction Container</h3>"

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    
    """
    Input sample:
    {
    "CHAS": { "0": 0 }, "RM": { "0": 6.575 },
    "TAX": { "0": 296 }, "PTRATIO": { "0": 15.3 },
    "B": { "0": 396.9 }, "LSTAT": { "0": 4.98 }
    }
    Output sample:
    { "prediction": [ 20.35373177134412 ] }
    """

    if request.method=="POST":
        clf = joblib.load("boston_housing_prediction.joblib")
        inference_payload = pd.DataFrame(request.json)
        
    
    if request.method=="GET":
        args = request.args
        CHAS = args.get("CHAS", default=0, type=int)
        RM = args.get("RM", default=0, type=float)
        TAX = args.get("TAX", default=0, type=float)
        PTRATIO = args.get("PTRATIO", default=0, type=float)
        B = args.get("B", default=0, type=float)
        LSTAT = args.get("LSTAT", default=0, type=float)

        input = ({
        "CHAS": { "0": f"{CHAS}" },
        "RM": { "0": f"{RM}" },
        "TAX": { "0": f"{TAX}" },
        "PTRATIO": { "0": f"{PTRATIO}" },
        "B": { "0": f"{B}" },
        "LSTAT": { "0": f"{LSTAT}" },
        })

        clf = joblib.load("boston_housing_prediction.joblib")
        inference_payload = pd.DataFrame(input)
    
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)