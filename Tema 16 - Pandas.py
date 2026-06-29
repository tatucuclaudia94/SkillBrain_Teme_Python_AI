import pandas as pd


# Creeaza DataFrame cu produse, pret si stoc

date = {
    "Produs": ["Laptop", "Telefon", "Mouse", "Monitor", "Tastatura"],
    "Pret": [3500, 2500, 120, 900, 200],
    "Stoc": [10, 15, 50, 8, 30]
}

df = pd.DataFrame(date)

print("DataFrame initial:")
print(df)


# Afiseaza produsele cu pret mai mare de 50

produse_scumpe = df[df["Pret"] > 50]

print("\nProduse cu pret > 50:")
print(produse_scumpe)


# Sorteaza produsele dupa pret descrescator

df_sortat = df.sort_values(by="Pret", ascending=False)

print("\nProduse sortate dupa pret descrescator:")
print(df_sortat)


# Adauga coloana TVA (19%)

df["TVA"] = df["Pret"] * 0.19

print("\nDataFrame cu TVA:")
print(df)


# Salveaza tabelul final in Excel

df.to_excel("produse.xlsx", index=False)

print("\nFisier Excel salvat: produse.xlsx")

