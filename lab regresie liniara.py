
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
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Încărcarea setului de date Diabetes
diabetes = load_diabetes()


X_bmi = diabetes.data[:, np.newaxis, 2]
y = diabetes.target


X_train, X_test, y_train, y_test = train_test_split(
    X_bmi, y,
    test_size=0.2,
    random_state=42 # Fixăm seed-ul pentru reproductibilitate
)


model_regresie = LinearRegression()
model_regresie.fit(X_train, y_train)


y_pred = model_regresie.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Eroarea pătratică medie (MSE) pe setul de test: {mse:.2f}")


plt.figure(figsize=(9, 6))


plt.scatter(X_test, y_test, color='blue', alpha=0.6, label='Date reale de test')


plt.plot(X_test, y_pred, color='red', linewidth=3, label='Linia de regresie')


plt.title('Regresie Liniară Simplă: BMI vs Progresia Diabetului', fontsize=14)
plt.xlabel('Body Mass Index (BMI - standardizat)', fontsize=12)
plt.ylabel('Scorul bolii (Target)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)


plt.show()


import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


diabetes = load_diabetes()


X_multi = diabetes.data[:, 2:4]
y = diabetes.target

# 3. Împărțirea datelor (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X_multi, y,
    test_size=0.2,
    random_state=42
)


model_multi = LinearRegression()
model_multi.fit(X_train, y_train)


print(f"Coeficient pentru BMI: {model_multi.coef_[0]:.2f}")
print(f"Coeficient pentru BP: {model_multi.coef_[1]:.2f}")
print(f"Termenul liber (Intercept): {model_multi.intercept_:.2f}")


y_pred = model_multi.predict(X_test)
scor_r2 = r2_score(y_test, y_pred)
print(f"Scorul R² pe setul de testare: {scor_r2:.4f}")