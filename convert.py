import csv
import pandas as pd
csv_file = "data.csv"
data = {
  "Outlook": ["Rainy", "Rainy", "Overcast","Sunny","Sunny","Sunny","Overcast","Rainy","Rainy","Sunny","Rainy","Overcast","Overcast","Sunny"],
  "Temp": ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool","Mild","Mild","Mild","Hot","Mild"],
  "Humidity": ["High", "High", "High","High","Normal","Normal","Normal","High","Normal","Normal","Normal","High","Normal","High"],
  "Windy":['n','y','n','n','n','y','y','n','n','n','y','y','n','y'],
  "Play":["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"]
}
df = pd.DataFrame.from_dict(data, orient="index")
df.to_csv("data.csv")
