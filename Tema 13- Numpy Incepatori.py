import numpy as np


# Exercitiul 1
# Creeaza un array 2D 5x5 cu numere aleatoare intre 1 si 100

matrice = np.random.randint(1, 101, (5, 5))

print("Matrice 5x5:")
print(matrice)



# Exercitiul 2
# Media, maximul si minimul fiecarui rand

print("\nStatistici pe randuri:")

for i, rand in enumerate(matrice):

    media = np.mean(rand)
    maxim = np.max(rand)
    minim = np.min(rand)

    print("Rand", i+1, ":", rand)
    print("Media:", media)
    print("Max:", maxim)
    print("Min:", minim)
    print()



# Exercitiul 3
# Normalizare array (x - media / deviatia standard)

def normalize_array(arr):

    media = np.mean(arr)
    dev_std = np.std(arr)

    rezultat = (arr - media) / dev_std

    return rezultat


vector = np.array([10, 20, 30, 40, 50])

print("Vector normalizat:")
print(normalize_array(vector))



# Exercitiul 4
# Produs scalar intre doua array-uri

def produs_scalar(a, b):

    return np.dot(a, b)


v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Produs scalar:", produs_scalar(v1, v2))



# Exercitiul 5
# Verifica daca matricea este simetrica

def matrice_simetrica(m):

    return np.array_equal(m, m.T)


matrice_test = np.array([
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
])

if matrice_simetrica(matrice_test):
    print("Matricea este simetrica")
else:
    print("Matricea nu este simetrica")

