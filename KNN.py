#ex 1

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data
print("forma set:", X.shape) # (nr_linii, nr_coloane)
print("nr exemple:",X.shape[0])
print("nr caracteristici:", X.shape[1])
print("denumiri atribute:",iris.feature_names)
print("numele claselor:",iris.target_names)

from sklearn.model_selection import train_test_split
X=iris.data
Y=iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2,
    random_state=42
)
print("forma X_train:", X_train.shape)
print("forma X_test :", X_test.shape)
print("forma y_train:", y_train.shape)
print("forma y_test :", y_test.shape)

scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)
print(X_train[:3])
print(X_train_scale[:3]) #le aduce in acelasi interval
#Z=(x-medie)/deviatie

#ex4

from sklearn.neighbors import KNeighborsClassifier
kmm=KNeighborsClassifier(n_neighbors=3)
kmm.fit(X_train_scale, y_train)
acuratete=kmm.score(X_test_scale, y_test) #trebuie sa testam daca a invatat
print("acuratete: ",acuratete)

#ex 5
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target


k_values = list(range(1, 16))
cv_scores = []


for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)

    scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())
    print(f"k = {k:2d} --> Acuratețe medie: {scores.mean():.4f}")


plt.figure(figsize=(10, 6))
plt.plot(k_values, cv_scores, marker='o', linestyle='-', color='b', markersize=8)
plt.title('Impactul valorii lui k asupra acurateții modelului KNN (Iris Dataset)')
plt.xlabel('Valoarea lui k (Numărul de vecini)')
plt.ylabel('Acuratețe Medie (Cross-Validation)')
plt.xticks(k_values)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
#ex6

from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


knn_optim = KNeighborsClassifier(n_neighbors=5)
knn_optim.fit(X_train, y_train)


y_pred = knn_optim.predict(X_test)


conf_matrix = confusion_matrix(y_test, y_pred)
print("Matricea de confuzie:\n", conf_matrix)



raport = classification_report(y_test, y_pred, target_names=iris.target_names)
print("\nRaport de clasificare:\n")
print(raport)

#ex7 tema pentru evaluare

import matplotlib.pyplot as plt


X_viz = X[:, 2:4]
y_viz = y

plt.figure(figsize=(9, 6))


scatter = plt.scatter(X_viz[:, 0], X_viz[:, 1], c=y_viz, cmap='viridis', edgecolor='k', s=80)

plt.title('Vizualizarea speciilor Iris (Lungime vs. Lățime Petală)', fontsize=14)
plt.xlabel('Lungime petală (cm)', fontsize=12)
plt.ylabel('Lățime petală (cm)', fontsize=12)


cbar = plt.colorbar(scatter, ticks=[0, 1, 2])
cbar.ax.set_yticklabels(iris.target_names)

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

#7.2
import numpy as np

print("=== Predictor Specie Iris ===")
print("Introduceți dimensiunile florii (valori numerice, ex: 5.2):")

try:

    sepal_length = float(input("Lungime sepală (cm): "))
    sepal_width = float(input("Lățime sepală (cm): "))
    petal_length = float(input("Lungime petală (cm): "))
    petal_width = float(input("Lățime petală (cm): "))


    floare_noua = np.array([[sepal_length, sepal_width, petal_length, petal_width]])


    index_predictie = knn_optim.predict(floare_noua)[0]
    nume_specie = iris.target_names[index_predictie]

    # 4. Afișăm rezultatul
    print("\n-------------------------------------------------")
    print(f"Florii introduse i-a fost atribuită specia: {nume_specie.upper()}")
    print("-------------------------------------------------")

except ValueError:
    print("\nEroare: Vă rugăm să introduceți exclusiv valori numerice valide (folosiți punctul pentru zecimale).")






