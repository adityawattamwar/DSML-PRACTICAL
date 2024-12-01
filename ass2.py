import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the House Price dataset
df = pd.read_csv("Datasets/House Data.csv")

print("Dataset Shape:", df.shape)
print("\nFeatures in the dataset:", list(df.columns))

# Computing statistics for each feature
print("\n=== Standard Deviation ===")
for column in df.columns:
    print(f"{column}: {df[column].std():.4f}")

print("\n=== Variance ===")
for column in df.columns:
    print(f"{column}: {df[column].var():.4f}")

print("\n=== Percentiles (25%, 50%, 75%) ===")
percentiles = df.describe().loc[['25%', '50%', '75%']]
for column in df.columns:
    print(f"\n{column}:")
    print(f"25th percentile: {percentiles.loc['25%', column]:.4f}")
    print(f"50th percentile: {percentiles.loc['50%', column]:.4f}")
    print(f"75th percentile: {percentiles.loc['75%', column]:.4f}")

# Creating histograms for each feature
num_features = len(df.columns)
num_rows = (num_features + 2) // 3  # Calculate number of rows needed
plt.figure(figsize=(15, 5 * num_rows))

for idx, column in enumerate(df.columns, 1):
    plt.subplot(num_rows, 3, idx)
    sns.histplot(data=df, x=column, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('house_price_distributions.png')
plt.close()

print("\nHistograms have been saved as 'house_price_distributions.png'")
