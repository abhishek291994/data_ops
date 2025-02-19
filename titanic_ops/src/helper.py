# Convert gender counts to a dictionary

def get_counts_by_gender(df):
    gender_counts = df["Sex"].value_counts().to_dict()
    return gender_counts