import pandas as pd
import numpy as np

# reproducibility
np.random.seed(42)

# size of dataset (adjust as needed)
rows = 100000   # huge dataset

# base features
sunlight = np.random.uniform(4, 8, rows)              # India-like sunlight hours
roof_area = np.random.uniform(400, 2000, rows)        # sqft
system_size = roof_area / 400                         # realistic sizing rule
temperature = np.random.uniform(20, 40, rows)         # °C

# deterministic generation formula
generation = system_size * sunlight * 30 * 0.75       # efficiency factor

# -------------------------------
# Add noise to make dataset realistic
# -------------------------------

# Gaussian noise (±5%)
gaussian_noise = np.random.normal(0, 0.05 * generation, rows)

# Multiplicative noise (±10%)
noise_factor = np.random.uniform(0.9, 1.1, rows)

# Feature-specific measurement errors
sunlight += np.random.normal(0, 0.2, rows)            # ±0.2 hr error
temperature += np.random.normal(0, 1.0, rows)         # ±1°C error

# Apply noise
generation_noisy = (generation + gaussian_noise) * noise_factor

# Introduce occasional outliers (cloudy month, maintenance downtime)
outlier_idx = np.random.choice(rows, size=int(0.01 * rows), replace=False)  # 1% outliers
generation_noisy[outlier_idx] *= np.random.uniform(0.5, 0.8, len(outlier_idx))

# -------------------------------
# Build final DataFrame
# -------------------------------
df = pd.DataFrame({
    "sunlight_hours": sunlight,
    "roof_area_sqft": roof_area,
    "system_size_kw": system_size,
    "temperature_c": temperature,
    "monthly_generation_kwh": generation_noisy
})

# save to CSV
df.to_csv("data/solar_data_large.csv", index=False)

print("✅ Huge noisy dataset generated at data/solar_data_large.csv")