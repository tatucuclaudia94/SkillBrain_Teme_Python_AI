import numpy as np


# creare array 5x5 cu numere aleatoare

matrice = np.random.randint(1,101,(5,5))

print("Matrice:")
print(matrice)


# media maximul si minimul fiecarui rand

media = np.mean(matrice, axis=1)

maxim = np.max(matrice, axis=1)

minim = np.min(matrice, axis=1)

print("Media randuri:", media)
print("Maxim randuri:", maxim)
print("Minim randuri:", minim)


# functie normalizare array

def normalizare(arr):

    return (arr - np.mean(arr)) / np.std(arr)


print("Array normalizat:")
print(normalizare(matrice))


# functie produs scalar

def produs_scalar(a,b):

    return np.dot(a,b)


a = np.array([1,2,3])
b = np.array([4,5,6])

print("Produs scalar:", produs_scalar(a,b))


# functie verificare matrice simetrica

def matrice_simetrica(m):

    return np.array_equal(m, m.T)


test = np.array([[1,2,3],
                 [2,5,6],
                 [3,6,9]])

print("Matrice simetrica:", matrice_simetrica(test))


