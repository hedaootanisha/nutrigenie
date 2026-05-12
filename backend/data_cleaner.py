import pandas as pd

# Load all datasets
df1 = pd.read_csv('../dataset/FOOD-DATA-GROUP1.csv')
df2 = pd.read_csv('../dataset/FOOD-DATA-GROUP2.csv')
df3 = pd.read_csv('../dataset/FOOD-DATA-GROUP3.csv')
df4 = pd.read_csv('../dataset/FOOD-DATA-GROUP4.csv')
df5 = pd.read_csv('../dataset/FOOD-DATA-GROUP5.csv')

# Combine
df = pd.concat([df1, df2, df3, df4, df5])

# Remove unwanted columns
df = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'], errors='ignore')

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv('../dataset/final_food_dataset.csv', index=False)

print("Dataset cleaned successfully!")

print(df.head())