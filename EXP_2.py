import pandas as pd

df = pd.read_csv(r"C:\Users\ARUNIMA\Downloads\archive (5)\worldcities.csv")  

subset_by_label = df.loc[0:5, ["city", "country"]]  
print("\nSubset using .loc[]:\n", subset_by_label)

subset_by_position = df.iloc[0:5, 0:3]
print("\nSubset using .iloc[]:\n", subset_by_position)


print("\nAggregated Statistics:")
print(df.aggregate({"population": ["mean", "sum", "min", "max"],
                    "id": ["count", "std"]}))  

grouped_df = df.groupby("city").agg({"population": ["mean", "sum", "count"]})  #
print("\nGrouped Data:\n", grouped_df)
