import pandas as pd

db1 = pd.read_csv('Cytotoxicity.csv')
db = pd.read_csv('out_new.csv')
df = db.iloc[: , 1:]
#print((df))
db1 = pd.merge(db1, df, on=['material'], how='left')
print(db1)

db1.to_csv('combined_new.csv')
