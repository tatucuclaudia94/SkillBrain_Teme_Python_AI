# Exercitiul 1
# Sorteaza lista de tuple (nume, varsta) dupa varsta

persoane = [
    ("Ana", 25),
    ("Mihai", 30),
    ("Elena", 22),
    ("George", 28)
]

persoane_sortate = sorted(persoane, key=lambda x: x[1])

print("Lista sortata dupa varsta:")
for p in persoane_sortate:
    print(p)


# Exercitiul 2
# Cautare binara intr-o lista sortata de scoruri

scoruri = [10, 20, 30, 40, 50, 60, 70]

def cautare_binara(lista, tinta):

    stanga = 0
    dreapta = len(lista) - 1

    while stanga <= dreapta:

        mijloc = (stanga + dreapta) // 2

        if lista[mijloc] == tinta:
            return True

        elif lista[mijloc] < tinta:
            stanga = mijloc + 1

        else:
            dreapta = mijloc - 1

    return False


scor_cautat = 40

if cautare_binara(scoruri, scor_cautat):
    print("Scorul exista in lista")
else:
    print("Scorul nu exista")


# Exercitiul 3
# Dict produse sortat dupa pret

produse = {
    "laptop": 3500,
    "telefon": 2500,
    "mouse": 150,
    "monitor": 1200
}

produse_sortate = sorted(produse.items(), key=lambda x: x[1])

print("\nProduse sortate dupa pret:")
for produs in produse_sortate:
    print(produs)


# Exercitiul 4
# Eliminare duplicate din lista folosind set

lista = [1, 2, 3, 2, 4, 5, 3, 6]

lista_fara_duplicate = list(set(lista))

print("\nLista fara duplicate:")
print(lista_fara_duplicate)


