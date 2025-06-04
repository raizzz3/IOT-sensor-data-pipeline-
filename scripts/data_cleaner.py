import pandas as pd, os
os.makedirs("data", exist_ok=True)
df = pd.read_csv("data/raw_sensor_data.csv")
df.dropna(inplace=True)
df['temperature'] = df['temperature'].astype(float)
df['humidity'] = df['humidity'].astype(float)
df.to_csv("data/clean_sensor_data.csv", index=False)
print("Cleaned data saved.")
