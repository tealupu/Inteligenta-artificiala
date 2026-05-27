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


