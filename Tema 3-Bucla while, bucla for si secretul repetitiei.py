# Exercitiul 1
# Bucla care cere un PIN pana este corect

pin_corect = "1234"
pin = ""

while pin != pin_corect:
    pin = input("Introdu PIN-ul de 4 cifre: ")

print("PIN corect. Acces permis.")


# Exercitiul 2
# Afiseaza o lista de 10 numere si numeroteaza-le

numere = [5, 12, 8, 20, 3, 15, 7, 9, 1, 11]

for i in range(len(numere)):
    print(i + 1, "-", numere[i])


# Exercitiul 3
# Piramida inversa

for i in range(5, 0, -1):
    print("*" * i)


# Exercitiul 4
# Suma numerelor pare intre 1 si 100

suma = 0

for i in range(1, 101):
    if i % 2 == 0:
        suma += i

print("Suma numerelor pare intre 1 si 100 este:", suma)