import numpy as np
import sns
from pandas import set_option

a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.dtype)
print(a.shape)
print(a[0])

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)
print(b[0, 2])

c = np.asarray([[1, 2], [3, 4]])
print(type(c))
print(c.dtype)
print(c.shape)

zero_array = np.zeros((3, 2))
print(zero_array)

one_array = np.ones((2, 2))
print(one_array)

constant_array = np.full((2, 2), 8)
print(constant_array)

identify_matrix = np.eye(3)
print(identify_matrix)

random_array = np.random.randn(1, 2)
print(random_array)

mu, sigma = 0, 0.1
gaussian_random = np.random.normal(mu, sigma, (3, 6))

first_5 = np.arange(5)
print(first_5)

#indexare
first_5 = np.arange(5)

array_to_slice = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
slice = array_to_slice[:, 0:3]
print(slice)

print(array_to_slice[0], [0])
slice[0][0] = 100
print(array_to_slice)

slice_copy = np.copy(array_to_slice[:, 0:3])
slice_copy[0][0] = 100
print(slice_copy[0][0])
print(array_to_slice[0][0])

#functii matematice
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))
my_array = np.arange(5)
powered = np.power(my_array, 3)
print(powered)

#produsul scalar
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v, w))

print(np.matmul(x, v))

print(np.matmul(x, v))

# operatii pe matrici

my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array.T)

my_array = np.array([[1., 2.], [3., 4.]])
print(np.linalg.inv(my_array))

x = np.array([[1, 2], [3, 4]])
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

print(np.sum(x, axis=(0, 1)))

y = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])

print(np.mean(y, axis=0))
print(np.mean(y, axis=1))

z = np.array([[10, 12, 5], [17, 11, 19]])
print(np.argmax(z, axis=1))

#broadcasting
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = m + v
print(y)

import matplotlib.pyplot as plt

'''x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)

plt.plot(x,y)
plt.xlabel('x axis label')
plt.ylabel('y axis label')

plt.title('Sine')
plt.legend(['Sine'])
plt.show()'''

import pandas as pd

'''data = pd.read_csv('data.csv')

set_option('display.max_columns',None)
set_option('display.max_rows',None)


print(data)
import os
print(os.getcwd())'''

data = pd.read_csv('data.csv')


print(data.loc[data['Age'] > 40, 'Age'].head(10))
print(data.loc[(data['Age'] < 25) & (data['Overall'] >=85)])
print("  ")
print(data.sort_values(by='Skill Moves', ascending=False))
print("  ")
#Contract Valid Until
print(data[data['Contract Valid Until']==2021])

randuri,coloane=data.shape
print(f'Avem {randuri} randuri si coloane {coloane} ')

nationalitati=data["Nationality"].value_counts().head()
print(nationalitati)

'''plt.figure(figsize=(10,10))

plt.pie(
    nationalitati,
    labels=nationalitati.index,
    autopct='%1.1f%%',
    startangle=90

)
plt.show()'''

medii=data.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()
print(f"Mediile sunt {medii}")

data["Position"]=data["Position"].fillna("UNKNOWN")
print(data["Position"])

medieclub=data.groupby("Club")["Overall"].mean()
club_top = medieclub.idxmax()
media_top = medieclub.max()

print(f"club cu cea mai mare medie Overall este: {club_top}")
print(f"medie overall: {media_top:.2f}")


def converteste(x):
    if pd.isna(x):
        return 0

    x = str(x).replace("€", "").strip()

    if "M" in x:
        return float(x.replace("M", "")) * 1_000_000

    elif "K" in x:
        return float(x.replace("K", "")) * 1_000

    else:
        return float(x)

data["Value_num"] = data["Value"].apply(converteste)
data["Wage_num"] = data["Wage"].apply(converteste)

data["is_underpaid"] = data["Wage_num"] < (data["Value_num"] / 100)
print(data[["Name", "Value", "Wage", "is_underpaid"]].head())


data["Scor_general"] = (
    0.3 * data["Overall"] +
    0.3 * data["Potential"] +
    0.2 * data["SprintSpeed"]
)
print(data[["Name", "Overall", "Potential", "SprintSpeed", "Scor_general"]].head())


