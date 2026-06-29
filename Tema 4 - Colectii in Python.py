# Tema 4 - Colectii in Python

# Exercitiul 1
# Lista cu filmele preferate

filme = [
    "The Conjuring",
    "Wrong Turn",
    "From",
    "The Hills Have Eyes",
    "Tarot",
    "Pet",
    "The Crooked Man",
    "Under the Shadow",
    "It Stains the Sands Red",
    "Terrifier",
    "A Dark Song"
]

print("Lista filme:")
print(filme)

print("\nFilme invers:")
print(list(reversed(filme)))

print("\nFilme in ordine alfabetica:")
print(sorted(filme))


# Exercitiul 2
# Tuplu cu coordonate GPS

coordonate = (45.7489, 21.2087, 46.7712, 23.6236)

print("\nCoordonate GPS:")
for coord in coordonate:
    print(coord)


# Exercitiul 3
# Set cu prenume si duplicat

prenume = {
    "Ana",
    "Maria",
    "Elena",
    "Ioana",
    "Andrei",
    "Bogdan",
    "Alex",
    "Cristina",
    "Mihai",
    "Daniel"
}

prenume.add("Ana")

print("\nSet de prenume:")
print(prenume)


# Exercitiul 4
# Dictionar produse si pret

produse = {
    "telefon": 1200,
    "casti": 150,
    "mouse": 45,
    "tastatura": 80,
    "cablu": 20
}

print("\nProduse cu pret peste 50 lei:")

for produs, pret in produse.items():
    if pret > 50:
        print(produs, "-", pret, "lei")


# Exercitiul 5
# Aplicatie elev + nota

elevi = {}

nume = input("\nIntrodu numele elevului: ")
nota = int(input("Introdu nota elevului: "))

elevi[nume] = nota

print("\nLista elevi:")
print(elevi)