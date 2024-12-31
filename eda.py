import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
print(os.path.exists("C:\Users\Aakash\Desktop\Github\Ecomlytics\data.csv"))

# Load the dataset
data_path = "C:\Users\Aakash\Desktop\Github\Ecomlytics\data.csv"
df = pd.read_csv(data_path)

# Basic exploration
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize correlations
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Pairplot for relationships
sns.pairplot(df)
plt.show()
