import pandas as pd

df = pd.read_csv('data2.csv', skipinitialspace=True, delimiter=",")

col = df.columns
col = [i.replace(' ', '_').lower() for i in col]
df.columns = col

df['возраст'] = df['возраст'].str.replace(',', '.')
df['возраст'] = df['возраст'].astype(float)
df['возраст'] = round(df['возраст'], 0).astype(int)


df_selected = df[['возраст', 'путешествует_с_детьми']]
print(df_selected.head(10))
