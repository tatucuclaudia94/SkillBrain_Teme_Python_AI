from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# functie frecventa relativa

def frecventa_relativa(text):

    cuvinte = text.lower().split()

    total = len(cuvinte)

    frecventa = Counter(cuvinte)

    frecventa_rel = {}

    for cuvant in frecventa:

        frecventa_rel[cuvant] = frecventa[cuvant] / total

    return frecventa_rel


# citire fisier txt

with open("articol.txt","r",encoding="utf-8") as f:

    text = f.read()


# calcul frecventa

freq = frecventa_relativa(text)

print("Frecvente relative:")

print(freq)


# generare wordcloud

wc = WordCloud(width=800,height=400,background_color="white")

wc.generate(text)


# afisare wordcloud

plt.imshow(wc)

plt.axis("off")

plt.show()

