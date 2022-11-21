import csv
import pandas as pd
import time
csv_file = "data.csv"
data = {
  "Outlook": ["Rainy", "Rainy", "Overcast","Sunny","Sunny","Sunny","Overcast","Rainy","Rainy","Sunny","Rainy","Overcast","Overcast","Sunny"],
  "Temp": ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool","Mild","Mild","Mild","Hot","Mild"],
  "Humidity": ["High", "High", "High","High","Normal","Normal","Normal","High","Normal","Normal","Normal","High","Normal","High"],
  "Windy":['no','yes','no','no','no','yes','yes','no','no','no','yes','yes','no','yes'],
  "Play":["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"]
}
print("Converting dataset to csv format...\n")
time.sleep(1)
df = pd.DataFrame.from_dict(data, orient="index")
df.to_csv("data.csv")
print("Convertion done. Now you can train your model\n")
