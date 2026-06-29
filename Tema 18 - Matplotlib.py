import matplotlib.pyplot as plt
import numpy as np


# Grafic temperaturi zilnice pentru o saptamana

zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
temperaturi = [20, 22, 19, 24, 26, 28, 25]

plt.figure()
plt.plot(zile, temperaturi, marker="o")
plt.title("Temperaturi zilnice")
plt.xlabel("Ziua")
plt.ylabel("Temperatura")
plt.grid(True)
plt.show()


# Grafic vanzari pe categorii (bare)

categorii = ["Electronice", "Haine", "Carti", "Jucarii"]
vanzari = [1500, 800, 400, 600]

plt.figure()
plt.bar(categorii, vanzari)
plt.title("Vanzari pe categorii")
plt.xlabel("Categorie")
plt.ylabel("Vanzari")
plt.show()


# Scatter plot cu puncte aleatoare

x = np.random.rand(100)
y = np.random.rand(100)

plt.figure()
plt.scatter(x, y)
plt.title("Scatter plot aleator")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# Doua grafice diferite intr-un subplot

fig, ax = plt.subplots(1, 2)

ax[0].plot(zile, temperaturi, marker="o")
ax[0].set_title("Temperaturi")

ax[1].bar(categorii, vanzari)
ax[1].set_title("Vanzari")

plt.show()


# Salvare grafic PNG si PDF

plt.figure()
plt.plot(zile, temperaturi, marker="o")
plt.title("Temperaturi salvate")

plt.savefig("grafic_temperaturi.png")
plt.savefig("grafic_temperaturi.pdf")

plt.show()

