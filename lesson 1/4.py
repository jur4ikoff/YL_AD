import pandas as pd

df = pd.read_csv('data4.csv', skipinitialspace=True, delimiter=",")
df['расстояние_кат'] = df['расстояние'].apply(
    lambda x: 'домашний_регион' if x <= 300 else ('недалеко_отдома' if x <= 700 else 'дальнее_путешествие'))

a = (df['расстояние_кат'].value_counts(normalize=True).apply(lambda x: x * 100))
a = round(a, 0)
a = a.astype(int)
print(a.to_frame())
