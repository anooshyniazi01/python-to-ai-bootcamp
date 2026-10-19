import pandas as pd
df = pd.read_csv("titanic.csv")
#How many women aged 18 or older in 3rd class survived?
q1 = df.loc[
    (df["Sex"] == "female")
    & (df["Pclass"] == 3)
    & (df["Age"] >= 18)
    & (df["Survived"] == 1)
]
print("Q1: 3rd class adult women who survived:", len(q1))
print(q1[["Name", "Age", "Pclass", "Survived"]].head())
#How many children under 12 in 2nd class survived?
q2 = df.loc[
    (df["Age"] < 12)
    & (df["Pclass"] == 2)
    & (df["Survived"] == 1)
]
print("\nQ2: 2nd class children under 12 who survived:", len(q2))
print(q2[["Name", "Age", "Pclass", "Survived"]].head())
