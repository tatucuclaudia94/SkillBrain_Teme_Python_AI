# Exercitiul 1
# Clasa Carte

class Carte:

    def __init__(self, titlu, autor, an):
        self.titlu = titlu
        self.autor = autor
        self.an = an


# Exercitiul 2
# Clasa Biblioteca

class Biblioteca:

    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)

    def cauta_dupa_autor(self, autor):
        print("\nCarti scrise de", autor)
        for carte in self.carti:
            if carte.autor == autor:
                print(carte.titlu, "-", carte.an)

    def afiseaza_toate(self):
        print("\nToate cartile din biblioteca:")
        for carte in self.carti:
            print(carte.titlu, "-", carte.autor, "-", carte.an)


# Testare aplicatie

biblioteca = Biblioteca()

carte1 = Carte("The Hobbit", "J.R.R. Tolkien", 1937)
carte2 = Carte("1984", "George Orwell", 1949)
carte3 = Carte("Animal Farm", "George Orwell", 1945)

biblioteca.adauga_carte(carte1)
biblioteca.adauga_carte(carte2)
biblioteca.adauga_carte(carte3)

biblioteca.afiseaza_toate()

biblioteca.cauta_dupa_autor("George Orwell")

