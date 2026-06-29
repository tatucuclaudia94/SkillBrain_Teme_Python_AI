import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Setare stil darkgrid pentru toate graficele

sns.set_theme(style="darkgrid")


# Histplot - distributie date aleatoare

date = np.random.normal(50, 10, 200)

sns.histplot(date, bins=20)

plt.title("Distributie date")
plt.show()


# Boxplot in functie de gen

df = pd.DataFrame({
    "Gen": np.random.choice(["Barbat", "Femeie"], 100),
    "Varsta": np.random.randint(18, 60, 100)
})

sns.boxplot(x="Gen", y="Varsta", data=df)

plt.title("Boxplot varsta in functie de gen")
plt.show()


# Pairplot pentru iris

iris = sns.load_dataset("iris")

sns.pairplot(iris)

plt.show()


# Heatmap corelatii pentru penguins

penguins = sns.load_dataset("penguins")

corelatii = penguins.corr(numeric_only=True)

sns.heatmap(corelatii, annot=True, cmap="coolwarm")

plt.title("Heatmap corelatii penguins")
plt.show()

