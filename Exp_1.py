import pandas as pd

df = pd.read_csv(r"C:\Users\ARUNIMA\Downloads\archive\Global_Music_Streaming_Listener_Preferences.csv")

print("Dataset Info:")
print(df.info())

print("\n First 5 Rows of the Dataset:")
print(df.head())

print("\n Missing Values in Each Column (Before Handling):")
print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype == 'object':  # If column is categorical
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:  # If column is numerical
        df[col].fillna(df[col].mean(), inplace=True)

print("\n Missing Values After Handling:")
print(df.isnull().sum())

numerical_cols = df.select_dtypes(include=['number'])

print("\n Statistical Measures:")
for col in numerical_cols.columns:
    print(f"\n {col}:")
    print(f"   Mean: {numerical_cols[col].mean()}")
    print(f"   Median: {numerical_cols[col].median()}")
    print(f"   Mode: {numerical_cols[col].mode()[0]}")  # Mode can have multiple values, taking the first one
    print(f"   Variance: {numerical_cols[col].var()}")
    print(f"   Standard Deviation: {numerical_cols[col].std()}")


print("\n Dataset Summary:")
print(df.describe())


df.to_csv(r"C:\Users\ARUNIMA\Downloads\archive\Cleaned_Global_Music_Streaming.csv", index=False)
print("\n Cleaned dataset saved as 'Cleaned_Global_Music_Streaming.csv'.")
