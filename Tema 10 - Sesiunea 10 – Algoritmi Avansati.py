# Exercitiul 1
# Sortare CSV folosind Merge Sort

import csv

def merge(left, right, index):
    rezultat = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i][index] <= right[j][index]:
            rezultat.append(left[i])
            i += 1
        else:
            rezultat.append(right[j])
            j += 1

    rezultat.extend(left[i:])
    rezultat.extend(right[j:])

    return rezultat


def merge_sort(data, index):

    if len(data) <= 1:
        return data

    mijloc = len(data) // 2

    left = merge_sort(data[:mijloc], index)
    right = merge_sort(data[mijloc:], index)

    return merge(left, right, index)


def sorteaza_csv(input_file, output_file, index_sort):

    with open(input_file, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))

    header = reader[0]
    rows = reader[1:]

    rows = merge_sort(rows, index_sort)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)



# Exercitiul 2
# Generare permutari ale unui cuvant

def permutari(cuvant):

    if len(cuvant) == 1:
        return [cuvant]

    rezultat = []

    for i in range(len(cuvant)):

        litera = cuvant[i]
        rest = cuvant[:i] + cuvant[i+1:]

        for p in permutari(rest):
            rezultat.append(litera + p)

    return rezultat


print("Permutari pentru 'abc':")
print(permutari("abc"))



# Exercitiul 3
# Suma subsecventelor cu memoizare

memo = {}

def suma_subsecvente(lista, index=0):

    if index == len(lista):
        return 0

    if index in memo:
        return memo[index]

    include = lista[index] + suma_subsecvente(lista, index + 1)
    exclude = suma_subsecvente(lista, index + 1)

    memo[index] = max(include, exclude)

    return memo[index]


print("Suma optimizata:", suma_subsecvente([3, 2, 7, 10]))



# Exercitiul 4
# Planificare activitati (Greedy Algorithm)

def planifica_activitati(intervale):

    intervale.sort(key=lambda x: x[1])

    rezultat = [intervale[0]]
    sfarsit = intervale[0][1]

    for start, end in intervale[1:]:

        if start >= sfarsit:
            rezultat.append((start, end))
            sfarsit = end

    return rezultat


activitati = [(1,3),(2,4),(3,5),(0,6),(5,7),(8,9)]

print("Activitati selectate:")
print(planifica_activitati(activitati))



# Exercitiul 5
# Problema celor 8 regine

N = 8

def este_sigur(tabla, rand, col):

    for i in range(col):
        if tabla[rand][i] == 1:
            return False

    i = rand
    j = col
    while i >= 0 and j >= 0:
        if tabla[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = rand
    j = col
    while i < N and j >= 0:
        if tabla[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def rezolva_regine(tabla, col):

    if col >= N:
        return True

    for i in range(N):

        if este_sigur(tabla, i, col):

            tabla[i][col] = 1

            if rezolva_regine(tabla, col + 1):
                return True

            tabla[i][col] = 0

    return False


def afiseaza_tabla(tabla):

    for rand in tabla:
        linie = ""

        for cell in rand:
            if cell == 1:
                linie += "Q "
            else:
                linie += ". "

        print(linie)


tabla = [[0]*N for _ in range(N)]

if rezolva_regine(tabla, 0):

    print("Solutie pentru 8 regine:")
    afiseaza_tabla(tabla)

else:
    print("Nu exista solutie")


