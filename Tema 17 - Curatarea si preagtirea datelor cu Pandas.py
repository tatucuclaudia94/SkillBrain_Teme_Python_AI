import pandas as pd
import numpy as np


# Creeaza DataFrame cu date zilnice pentru o luna

date = pd.date_range(start="2024-01-01", periods=30)

df = pd.DataFrame({
    "Data": date,
    "Oras": np.random.choice(["Cluj", "Timisoara", "Bucuresti"], 30),
    "Produs": np.random.choice(["Laptop", "Telefon", "Mouse"], 30),
    "Vanzari": np.random.randint(10, 200, 30)
})

print("DataFrame initial:")
print(df)


# Filtreaza datele pentru o saptamana

saptamana = df[(df["Data"] >= "2024-01-08") & (df["Data"] <= "2024-01-14")]

print("\nDate pentru saptamana selectata:")
print(saptamana)


# Creeaza pivot table cu media vanzarilor pe oras si produs

pivot = pd.pivot_table(
    df,
    values="Vanzari",
    index="Oras",
    columns="Produs",
    aggfunc="mean"
)

print("\nPivot table (media vanzarilor):")
print(pivot)


# Eliminarea randurilor cu valori lipsa

df_curat = df.dropna()

print("\nDataFrame fara valori lipsa:")
print(df_curat)


# Functie care curata datele

def curata_date(dataframe):

    dataframe = dataframe.dropna()

    dataframe = dataframe.drop_duplicates()

    return dataframe


df_final = curata_date(df)

print("\nDataFrame curatat:")
print(df_final)

