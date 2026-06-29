from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


# incarcare dataset iris

iris = load_iris()

X = iris.data
y = iris.target


# impartire train test

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2
)


# model SVM

svm = SVC()

svm.fit(X_train, y_train)

svm_score = svm.score(X_test, y_test)

print("SVM score:", svm_score)


# model RandomForest

rf = RandomForestClassifier()

rf.fit(X_train, y_train)

rf_score = rf.score(X_test, y_test)

print("RandomForest score:", rf_score)


# model KNN

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

knn_score = knn.score(X_test, y_test)

print("KNN score:", knn_score)


# pipeline StandardScaler + RandomForest

pipeline = Pipeline([
("scaler", StandardScaler()),
("rf", RandomForestClassifier())
])

pipeline.fit(X_train, y_train)

pipeline_score = pipeline.score(X_test, y_test)

print("Pipeline score:", pipeline_score)


# GridSearch pentru KNN

param_grid = {
"n_neighbors":[1,3,5,7,9]
}

grid = GridSearchCV(
KNeighborsClassifier(),
param_grid,
cv=5
)

grid.fit(X_train, y_train)

print("Best KNN neighbors:", grid.best_params_)

print("Best score:", grid.best_score_)


# raport comparare modele

print("Model comparison")

print("SVM:", svm_score)

print("RandomForest:", rf_score)

print("KNN:", knn_score)

