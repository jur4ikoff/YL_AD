import pandas as pd

df = pd.read_csv('data1.csv', skipinitialspace=True, delimiter=";")
new_df = df.dropna()
print(*new_df.shape)