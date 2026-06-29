import numpy as np


# 1 milion de numere aleatoare
# suma numerelor divizibile cu 7

numere = np.random.randint(1, 1000000, 1000000)

numere_divizibile = numere[numere % 7 == 0]

suma = np.sum(numere_divizibile)

print("Suma numerelor divizibile cu 7:", suma)


# matrice 1000x1000
# normalizare fiecare coloana

matrice = np.random.rand(1000, 1000)

media = np.mean(matrice, axis=0)

deviatia = np.std(matrice, axis=0)

matrice_normalizata = (matrice - media) / deviatia

print("Normalizare coloane finalizata")


# simulare imagine RGB 1920x1080
# aplicare contrast

imagine = np.random.randint(0, 256, (1080, 1920, 3), dtype=np.uint8)

contrast = imagine * 1.5

contrast = np.clip(contrast, 0, 255).astype(np.uint8)

print("Contrast aplicat imaginii")


# matrice 3D 10x10x10
# suma pe axa Z

matrice3d = np.random.randint(1, 100, (10, 10, 10))

suma_z = np.sum(matrice3d, axis=2)

print("Suma pe axa Z:")
print(suma_z)


# 50 milioane numere
# folosim tip eficient de memorie

numere_mari = np.arange(50000000, dtype=np.int32)

total = np.sum(numere_mari)

print("Suma celor 50 milioane numere:", total)

