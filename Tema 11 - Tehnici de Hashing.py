# Exercitiul 1
# Sistem simplu de indexare PDF folosind hash

import hashlib

carti = {}

def indexeaza_carte(nume, continut):

    hash_carte = hashlib.md5(continut.encode()).hexdigest()

    carti[nume] = hash_carte

    print("Carte indexata:", nume)


indexeaza_carte("Python_Basics.pdf", "Introducere in Python si programare")
indexeaza_carte("AI_Guide.pdf", "Machine learning si inteligenta artificiala")

print("Index carti:", carti)



# Exercitiul 2
# Verificare duplicate in lista de 10.000 de nume

def verifica_duplicate(lista):

    vazute = set()

    duplicate = set()

    for nume in lista:

        if nume in vazute:
            duplicate.add(nume)
        else:
            vazute.add(nume)

    return duplicate


lista_nume = ["Ana", "Maria", "Ion", "Ana", "George", "Maria"]

print("Duplicate gasite:", verifica_duplicate(lista_nume))



# Exercitiul 3
# Cele mai frecvente 5 cuvinte folosind Counter

from collections import Counter

text = """
Python este un limbaj de programare foarte popular.
Python este folosit pentru AI, web si analiza de date.
"""

cuvinte = text.lower().split()

counter = Counter(cuvinte)

print("Top 5 cuvinte:")
print(counter.most_common(5))



# Exercitiul 4
# Implementare simpla HashMap cu chaining

class HashMap:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):

        index = self.hash_function(key)

        for pair in self.table[index]:

            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def get(self, key):

        index = self.hash_function(key)

        for pair in self.table[index]:

            if pair[0] == key:
                return pair[1]

        return None


h = HashMap()

h.put("apple", 10)
h.put("banana", 20)

print("Valoare apple:", h.get("apple"))



# Exercitiul 5
# Sistem auto-complete folosind hashing pe prefixe

autocomplete = {}

def adauga_cuvant(cuvant):

    for i in range(1, len(cuvant)+1):

        prefix = cuvant[:i]

        if prefix not in autocomplete:
            autocomplete[prefix] = []

        autocomplete[prefix].append(cuvant)


adauga_cuvant("python")
adauga_cuvant("programare")
adauga_cuvant("proiect")

print("Sugestii pentru 'pro':")
print(autocomplete.get("pro", []))


