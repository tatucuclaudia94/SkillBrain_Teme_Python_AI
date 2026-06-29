# Exercitiul 1
utilizator = input("Utilizator: ")
parola = input("Parola: ")

if utilizator == "admin" and parola == "1234":
    print("Acces permis pentru administrator.")
elif utilizator == "guest" and parola == "guest":
    print("Acces permis pentru vizitator.")
else:
    print("Acces respins.")

    #Exercitiul 2 
    # Tema 2 - Meniu interactiv

print("Meniu principal")
print("1. Adaugare")
print("2. Stergere")
print("3. Vizualizare")
print("4. Cautare")
print("5. Iesire")

optiune = input("Alege o optiune: ")

if optiune == "1":
    print("Ai ales adaugare.")
elif optiune == "2":
    print("Ai ales stergere.")
elif optiune == "3":
    print("Ai ales vizualizare.")
elif optiune == "4":
    print("Ai ales cautare.")
elif optiune == "5":
    print("Program inchis.")
else:
    print("Optiune invalida.")