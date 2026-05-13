
import pandas as pd
from pandas import set_option
from pandas.core.common import fill_missing_names

data = pd.read_csv('StudentsPerformance.csv')
'''set_option('display.max_columns',None)
set_option('display.max_rows',None)'''
print(data.head())
#afisez dimensiune
print (data.shape)
print(data.info)
print(data.isnull().sum()) #val libere in feicare coloana
print(data.describe())#statistici descriptive (medie,deviatie,min-max)
print("\n Var Numerice:")
print(data.select_dtypes(['int64','float64']))
print("\n Var Categorice:")
print(data.select_dtypes(include=['object','category','string']))
coloanenum = data.select_dtypes(include=['number']).columns
coloanecateg=data.select_dtypes(include=['object','category','string']).columns
for col in coloanenum:
    data.col=data[col].fillna(data[col].median)


for col in coloanecateg:
    data.col=data[col].fillna('UNKNOWN')
    print("\n inlocuire cu unknown+mediana")
    print(data.head)
