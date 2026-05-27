
from sklearn.linear_model import LinearRegression

from sklearn.datasets import load_diabetes
#y=mx+b
from sklearn.linear_model import LinearRegression
import numpy as np
x=np.array([[1],[2],[3],[4]])
y=np.array([5,6,7,8])
model=LinearRegression()
model.fit(x,y)
predictie=model.predict([[5]])
print(predictie)
diabetes = load_diabetes()
import pandas as pd
df=pd.DataFrame(diabetes.data, columns =diabetes.feature_names)

df['target']=diabetes.target
print(df.head())
print(df.describe())
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.hist(['bmi'],bins=20)
plt.title('Histogram de bmi')
plt.xlabel('bmi')
plt.ylabel('Frecventa')
plt.show()

#ex6

plt.figure(figsize=(8,6))
plt.scatter(df['bmi'],df['age'],c=df['target'],cmap="viridis")
plt.title('bmi si varsta')
plt.xlabel('bmi')
plt.ylabel('Varsta')
plt.colorbar(label='Target')
plt.show()

#ex7 si 8 tema