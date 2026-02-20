import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path

# ---- Resolve project root safely ----
BASE_DIR = Path(__file__).resolve().parent

data_path = BASE_DIR / "data" / "solar_data.csv"
model_path = BASE_DIR / "models" / "energy_model.pkl"

# ---- Load Dataset ----
df = pd.read_csv(data_path)

X = df[["sunlight_hours", "roof_area_sqft", "system_size_kw", "temperature_c"]]
y = df["monthly_generation_kwh"]

# ---- Train/Test Split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---- Train Model ----
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"✅ Model trained successfully | R² Score: {score:.4f}")

# ---- Save Model ----
joblib.dump(model, model_path)
print(f"✅ Model saved at: {model_path}")