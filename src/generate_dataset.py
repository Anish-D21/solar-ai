import pandas as pd
import numpy as np

np.random.seed(42)

rows = 500

sunlight = np.random.uniform(4, 8, rows)              # India-like sunlight hours
roof_area = np.random.uniform(400, 2000, rows)        # sqft
system_size = roof_area / 400                         # realistic sizing rule
temperature = np.random.uniform(20, 40, rows)

# Realistic solar generation formula
generation = system_size * sunlight * 30 * 0.75       # efficiency factor

df = pd.DataFrame({
    "sunlight_hours": sunlight,
    "roof_area_sqft": roof_area,
    "system_size_kw": system_size,
    "temperature_c": temperature,
    "monthly_generation_kwh": generation
})

df.to_csv("data/solar_data.csv", index=False)

print("✅ Dataset generated at data/solar_data.csv")