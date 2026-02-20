import joblib
import pandas as pd
import os

# Load trained model
MODEL_PATH = os.path.join("models", "energy_model.pkl")
model = joblib.load(MODEL_PATH)


def predict_generation(sun_hours, roof_area, system_size, temperature):
    """
    Predict monthly solar energy generation (kWh)
    using the SAME feature schema used during training.
    """

    # ⚠️ Column names MUST match training dataset exactly
    input_df = pd.DataFrame([{
        "sunlight_hours": sun_hours,
        "roof_area_sqft": roof_area,
        "system_size_kw": system_size,
        "temperature_c": temperature
    }])

    prediction = model.predict(input_df)[0]

    return round(prediction, 2)