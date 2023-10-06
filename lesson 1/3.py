import pandas as pd

df = pd.read_csv('data3.csv', skipinitialspace=True, delimiter=",")

df['возраст_кат'] = df['возраст'].apply(lambda x: 'менее_30' if x <= 30 else 'более_30')

a = (df['возраст_кат'].value_counts(normalize=True).apply(lambda x: x * 100))
a = round(a, 0)
a = a.astype(int)
print(a.to_frame())
