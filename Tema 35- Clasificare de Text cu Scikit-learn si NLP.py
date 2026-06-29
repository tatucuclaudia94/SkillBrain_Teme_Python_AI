from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


# dataset simplu spam ham

mesaje = [
"castiga bani rapid",
"oferta speciala acum",
"cumpara acum",
"salut ce faci",
"ne vedem maine",
"trimite documentul",
"ai castigat premiul",
"oferta limitata",
"hai la cafea",
"discutam proiectul"
]

etichete = [
"spam","spam","spam",
"ham","ham","ham",
"spam","spam","ham","ham"
]


# impartire train test

X_train, X_test, y_train, y_test = train_test_split(
mesaje, etichete, test_size=0.2
)


# vectorizare TF-IDF

tfidf = TfidfVectorizer()

X_train_tfidf = tfidf.fit_transform(X_train)

X_test_tfidf = tfidf.transform(X_test)


# model NaiveBayes

nb = MultinomialNB()

nb.fit(X_train_tfidf, y_train)

pred_nb = nb.predict(X_test_tfidf)

print("TFIDF NaiveBayes:", accuracy_score(y_test, pred_nb))


# vectorizare CountVectorizer

cv = CountVectorizer()

X_train_cv = cv.fit_transform(X_train)

X_test_cv = cv.transform(X_test)


# model NaiveBayes cu CountVectorizer

nb2 = MultinomialNB()

nb2.fit(X_train_cv, y_train)

pred_nb2 = nb2.predict(X_test_cv)

print("CountVectorizer NaiveBayes:", accuracy_score(y_test, pred_nb2))


# model SVM

svm = LinearSVC()

svm.fit(X_train_cv, y_train)

pred_svm = svm.predict(X_test_cv)

print("SVM score:", accuracy_score(y_test, pred_svm))


# sistem spam ham pentru utilizator

mesaj_user = input("Scrie mesaj: ")

vector = cv.transform([mesaj_user])

predictie = svm.predict(vector)

print("Clasificare mesaj:", predictie[0])

