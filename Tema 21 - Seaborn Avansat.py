import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Setare stil grafic

sns.set_theme(style="darkgrid")


# Creeaza DataFrame pentru salarii

df = pd.DataFrame({
    "Experienta": np.random.choice(["Junior", "Mid", "Senior"], 100),
    "Sex": np.random.choice(["Barbat", "Femeie"], 100),
    "Salariu": np.random.randint(3000, 12000, 100),
    "Varsta": np.random.randint(22, 50, 100),
    "Luna": np.random.choice(["Ian", "Feb", "Mar", "Apr", "Mai", "Iun"], 100)
})


# Violinplot salariu pe experienta cu split pe sexe

sns.violinplot(x="Experienta", y="Salariu", hue="Sex", data=df, split=True)

plt.title("Violinplot salariu pe experienta")
plt.show()


# FacetGrid distributie salarii pe luni si sexe

g = sns.FacetGrid(df, col="Sex", row="Luna")

g.map(sns.histplot, "Salariu")

plt.show()


# Heatmap primele 50 linii

date = np.random.rand(100, 5)

df_heat = pd.DataFrame(date)

sns.heatmap(df_heat.head(50), cmap="coolwarm")

plt.title("Heatmap primele 50 linii")
plt.show()


# Pairplot date generate artificial

date_personale = pd.DataFrame({
    "Varsta": np.random.randint(20, 50, 50),
    "Salariu": np.random.randint(3000, 10000, 50),
    "Ore_lucrate": np.random.randint(30, 50, 50)
})

sns.pairplot(date_personale)

plt.show()


# Barplot salariu mediu sub 30 vs peste 30

df["Grupa_varsta"] = df["Varsta"].apply(lambda x: "Sub 30" if x < 30 else "Peste 30")

sns.barplot(x="Grupa_varsta", y="Salariu", data=df)

plt.title("Salariu mediu pe grupa de varsta")
plt.show()

