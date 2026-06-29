from sklearn.datasets import load_diabetes
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier


# incarcare dataset diabetes

diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target


# impartire date train test

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2
)


# model regresie

model = LinearRegression()

model.fit(X_train, y_train)


# scor R2

score = model.score(X_test, y_test)

print("R2 score:", score)


# incarcare dataset iris

iris = load_iris()

X = iris.data
y = iris.target


# impartire date

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2
)


# model clasificare KNN

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)


# scor clasificare

score = knn.score(X_test, y_test)

print("Accuracy:", score)


# predictie pentru o floare noua

predictie = knn.predict([[5.1,3.5,1.4,0.2]])

print("Predictie iris:", predictie)

