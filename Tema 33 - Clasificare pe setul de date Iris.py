import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


# incarcare dataset

iris = load_iris()

X = iris.data
y = iris.target


# impartire train test

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2
)


# KNN cu mai multe valori

neighbors = [1,3,5,7,9]
scores_knn = []

for n in neighbors:

    knn = KNeighborsClassifier(n_neighbors=n)

    knn.fit(X_train, y_train)

    score = knn.score(X_test, y_test)

    scores_knn.append(score)

    print("KNN neighbors", n, "score:", score)


# model SVC

svc = SVC()

svc.fit(X_train, y_train)

svc_score = svc.score(X_test, y_test)

print("SVC score:", svc_score)


# model RandomForest

rf = RandomForestClassifier()

rf.fit(X_train, y_train)

rf_score = rf.score(X_test, y_test)

print("RandomForest score:", rf_score)


# grafic comparativ

models = ["SVC","RandomForest","KNN"]
scores = [svc_score, rf_score, max(scores_knn)]

plt.bar(models, scores)

plt.title("Comparatie modele Iris")

plt.ylabel("Accuracy")

plt.show()
