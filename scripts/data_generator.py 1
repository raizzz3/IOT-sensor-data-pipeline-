import csv, random, datetime, os
os.makedirs("data", exist_ok=True)
with open("data/raw_sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature", "humidity", "light"])
    for _ in range(100):
        writer.writerow([
            datetime.datetime.now().isoformat(),
            round(random.uniform(20, 35), 2),
            round(random.uniform(30, 70), 2),
            random.randint(100, 800)
        ])
