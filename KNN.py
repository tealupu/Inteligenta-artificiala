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
    X, Y, test_size=0.2, #pt ca e 20%
    random_state=42 #impartire aleatorie ca rezultatele sa fie aceleasi pe fiecare rulare
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
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt

k_values = []
accuracies = []

# Testarea valorilor k de la 1 la 15
for k in range(1, 16):

    # Crearea modelului
    model = KNeighborsClassifier(n_neighbors=k)

    # Antrenarea modelului
    model.fit(X_train, y_train)

    # Predicții
    y_pred = model.predict(X_test)

    # Calculul acurateții
    acc = accuracy_score(y_test, y_pred)

    # Salvarea rezultatelor
    k_values.append(k)
    accuracies.append(acc)

    print(f"k = {k}, acuratețe = {acc:.4f}")

# Graficul acurateții
plt.plot(k_values, accuracies, marker='o')

plt.xlabel("Valoarea lui k")
plt.ylabel("Acuratețe")
plt.title("Acuratețea modelului KNN în funcție de k")

plt.xticks(range(1, 16))
plt.grid(True)

plt.show()

#ex6
report=classification_report(y_test, y_pred, target_names=iris.target_names)
print(report)

#ex7 tema pentru evaluare








