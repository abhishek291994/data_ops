import pandas as pd

from helper import get_counts_by_gender

# URL of the dataset

# path= "data/titanic.csv"
path = "/Users/abhishekbhagwat/Study/data_ops/data/titanic.csv"

# Read the CSV file
df = pd.read_csv(path)

# Display the first 5 rows
print(df.head())


# ETL code and functions
# function to give count by gender

gender_counts = get_counts_by_gender(df)
gender_counts = df["Sex"].value_counts().to_dict()

# Display result
print(gender_counts)


print("This pr changes")

