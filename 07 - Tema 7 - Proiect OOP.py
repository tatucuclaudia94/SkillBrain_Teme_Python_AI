import csv


# Lista studenti
studenti = []


# Exercitiul 1
# Adauga student

def adauga_student():
    nume = input("Nume student: ")
    email = input("Email student: ")
    nota = float(input("Nota student: "))

    student = {
        "nume": nume,
        "email": email,
        "nota": nota
    }

    studenti.append(student)
    print("Student adaugat.")


# Exercitiul 2
# Afiseaza toti studentii

def afiseaza_studenti():

    if not studenti:
        print("Nu exista studenti.")
        return

    print("\nLista studenti:")
    for s in studenti:
        print(s["nume"], "-", s["email"], "-", s["nota"])


# Exercitiul 3
# Sterge student dupa email

def sterge_student():

    email = input("Email student de sters: ")

    for s in studenti:
        if s["email"] == email:
            studenti.remove(s)
            print("Student sters.")
            return

    print("Studentul nu exista.")


# Exercitiul 4
# Cel mai bun student

def cel_mai_bun_student():

    if not studenti:
        print("Nu exista studenti.")
        return

    best = max(studenti, key=lambda x: x["nota"])

    print("\nCel mai bun student:")
    print(best["nume"], "-", best["nota"])


# Exercitiul 5
# Salvare CSV

def salveaza_fisiere():

    with open("studenti.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nume", "email", "nota"])

        for s in studenti:
            writer.writerow([s["nume"], s["email"], s["nota"]])

    with open("note.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["email", "nota"])

        for s in studenti:
            writer.writerow([s["email"], s["nota"]])

    with open("rapoarte.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nume", "nota"])

        for s in studenti:
            writer.writerow([s["nume"], s["nota"]])

    print("Fisiere CSV salvate.")


# Exercitiul 6
# Incarcare CSV

def incarca_studenti():

    try:
        with open("studenti.csv", "r") as f:
            reader = csv.DictReader(f)

            studenti.clear()

            for row in reader:
                studenti.append({
                    "nume": row["nume"],
                    "email": row["email"],
                    "nota": float(row["nota"])
                })

        print("Studenti incarcati din fisier.")

    except FileNotFoundError:
        print("Fisierul nu exista.")


# Exercitiul 7
# Meniu interactiv

while True:

    print("\nMeniu:")
    print("1. Adauga student")
    print("2. Afiseaza toti studentii")
    print("3. Sterge student dupa email")
    print("4. Cel mai bun student")
    print("5. Salveaza in CSV")
    print("6. Incarca din CSV")
    print("7. Iesire")

    opt = input("Alege optiunea: ")

    if opt == "1":
        adauga_student()

    elif opt == "2":
        afiseaza_studenti()

    elif opt == "3":
        sterge_student()

    elif opt == "4":
        cel_mai_bun_student()

    elif opt == "5":
        salveaza_fisiere()

    elif opt == "6":
        incarca_studenti()

    elif opt == "7":
        print("Program inchis.")
        break

    else:
        print("Optiune invalida.")

