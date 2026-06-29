# Exercitiul 1
# Gestiune angajati

angajati = [
    {"nume": "Ana", "salariu": 4500, "pozitie": "Programator"},
    {"nume": "Bogdan", "salariu": 5200, "pozitie": "Manager"},
    {"nume": "Maria", "salariu": 3800, "pozitie": "Tester"},
    {"nume": "Alex", "salariu": 6100, "pozitie": "Arhitect Software"}
]

def salariu_mediu(lista_angajati):
    total = 0
    for angajat in lista_angajati:
        total += angajat["salariu"]
    return total / len(lista_angajati)

def afisare_peste_medie(lista_angajati):
    medie = salariu_mediu(lista_angajati)

    print("\nSalariu mediu:", medie)

    print("\nAngajati cu salariu peste medie:")
    for angajat in lista_angajati:
        if angajat["salariu"] > medie:
            print(angajat["nume"], "-", angajat["salariu"], "-", angajat["pozitie"])

afisare_peste_medie(angajati)


# Exercitiul 2
# Text Analytics

def text_analytics(text):

    cuvinte = text.split()

    numar_cuvinte = len(cuvinte)

    cel_mai_lung = max(cuvinte, key=len)

    contine_python = "python" in text.lower()

    return numar_cuvinte, cel_mai_lung, contine_python


text = input("\nIntrodu un text: ")

nr_cuvinte, cuvant_lung, apare_python = text_analytics(text)

print("Numar de cuvinte:", nr_cuvinte)
print("Cel mai lung cuvant:", cuvant_lung)
print("Contine 'python':", apare_python)


# Exercitiul 3
# Cos de cumparaturi

cos = []

def adauga_produs(nume, pret):
    cos.append({"produs": nume, "pret": pret})

def total_cu_tva():
    total = 0
    for produs in cos:
        total += produs["pret"]

    tva = total * 0.19
    return total + tva

def bon_fiscal():

    print("\nBon fiscal")
    print("----------------")

    total = 0

    for produs in cos:
        print(produs["produs"], "-", produs["pret"], "lei")
        total += produs["pret"]

    print("----------------")
    print("Total fara TVA:", total)

    tva = total * 0.19
    print("TVA:", round(tva, 2))

    print("Total de plata:", round(total + tva, 2))


adauga_produs("Laptop", 3500)
adauga_produs("Mouse", 80)
adauga_produs("Tastatura", 150)

bon_fiscal()

print("Total cu TVA:", round(total_cu_tva(), 2))