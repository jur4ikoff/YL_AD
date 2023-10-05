import pandas as pd
import numpy as np

df = pd.read_csv('lesson 1/data1.csv', skipinitialspace=True, delimiter=";")

# cat_feature = df.drop(['Возраст', 'Расстояние'], axis=1).columns
#
# for i in cat_feature:
#     print(df[i].value_counts())

# df['new'] = df['Возраст'].apply(lambda x: 'менее_30' if x <= 30 else 'более_30')
# print(df['new'].value_counts())

# print(df.isna().sum()) колво пропусков

# print(df['Расстояние'].sum()) мин макс сумма
# print(df['Расстояние'].agg(['sum', 'min', 'max']))
# print(df.agg({'Расстояние': ['sum', 'mean'], 'Возраст': ['mean']}))
#print(df.groupby(['Пол']).agg({'Расстояние': ['sum', 'mean'], 'Возраст': ['mean', 'min']}))