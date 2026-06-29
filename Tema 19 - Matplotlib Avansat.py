import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Animatie functie trigonometrica (efect puls)

x = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))

def update(frame):
    line.set_ydata(np.sin(x + frame))
    return line,

anim = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100), interval=50)

plt.title("Animatie functie trigonometrica")
plt.show()


# Subplot comparare vanzari pe ani

ani = ["2021", "2022", "2023", "2024"]
vanzari = [120, 150, 170, 200]

fig, ax = plt.subplots(1, 2)

ax[0].plot(ani, vanzari, marker="o")
ax[0].set_title("Vanzari - Linie")

ax[1].bar(ani, vanzari)
ax[1].set_title("Vanzari - Bare")

plt.show()


# Heatmap temperaturi pe o luna

temperaturi = np.random.randint(15, 35, (30, 7))

plt.figure()
plt.imshow(temperaturi, cmap="hot", aspect="auto")
plt.colorbar()
plt.title("Heatmap temperaturi luna")
plt.xlabel("Ziua saptamanii")
plt.ylabel("Ziua lunii")
plt.show()


# Fill_between intre doua serii

x = np.arange(10)

serie1 = np.random.randint(50, 100, 10)
serie2 = np.random.randint(30, 80, 10)

plt.figure()
plt.plot(x, serie1, label="Serie 1")
plt.plot(x, serie2, label="Serie 2")

plt.fill_between(x, serie1, serie2, alpha=0.3)

plt.legend()
plt.title("Variatie intre doua serii")
plt.show()


# Stil dark pentru grafice

plt.style.use("dark_background")

plt.figure()
plt.plot(ani, vanzari, marker="o")
plt.title("Grafic stil dark")
plt.show()

