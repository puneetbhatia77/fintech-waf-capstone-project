import pickle
import pandas as pd

def load_model():
    with open("ml_model/model.pkl", "rb") as f:
        return pickle.load(f)

def predict(input_data):
    model = load_model()
    df = pd.DataFrame([input_data])
    prediction = model.predict_proba(df)[:,1]
    return float(prediction[0])
