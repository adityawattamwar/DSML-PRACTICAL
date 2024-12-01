import pandas as pd

# Load the Titanic dataset
file_path = "D://DSML PRACTICAL//Datasets//Titanic.csv"
df = pd.read_csv(file_path)

# Read data and display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Indexing and selecting data (e.g., selecting rows where Age > 30)
selected_data = df[df['Age'] > 30]
print("\nRows where Age > 30:")
print(selected_data)

# Sorting data by Fare
sorted_data = df.sort_values(by='Fare', ascending=False)
print("\nTop rows sorted by Fare (descending):")
print(sorted_data.head())

# Describing attributes of data
description = df.describe()
print("\nDescription of dataset attributes:")
print(description)

# Checking data types of each column
data_types = df.dtypes
print("\nData types of each column:")
print(data_types)
