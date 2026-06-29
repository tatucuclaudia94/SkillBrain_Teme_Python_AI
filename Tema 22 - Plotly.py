import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


# Scatter plot cu date personale (varsta vs venit)

df = pd.DataFrame({
    "Varsta": [25, 30, 35, 40, 28],
    "Venit": [3000, 4500, 6000, 8000, 4200]
})

fig = px.scatter(df, x="Varsta", y="Venit", title="Varsta vs Venit")
fig.show()


# Dashboard simplu cu 3 grafice interactive

categorii = ["Electronice", "Haine", "Carti", "Jucarii"]
vanzari = [1500, 800, 400, 600]

fig_bar = px.bar(x=categorii, y=vanzari, title="Vanzari pe categorii")
fig_bar.show()

luni = ["Ian", "Feb", "Mar", "Apr", "Mai", "Iun"]
vanzari_luni = [200, 250, 300, 280, 320, 350]

fig_line = px.line(x=luni, y=vanzari_luni, title="Vanzari lunare")
fig_line.show()

fig_pie = px.pie(values=vanzari, names=categorii, title="Distributie vanzari")
fig_pie.show()


# Boxplot pentru 4 categorii

df_box = pd.DataFrame({
    "Categorie": np.random.choice(["A", "B", "C", "D"], 100),
    "Valoare": np.random.randint(10, 100, 100)
})

fig_box = px.box(df_box, x="Categorie", y="Valoare", title="Boxplot categorii")
fig_box.show()


# Heatmap cu date random 10x10

date = np.random.rand(10, 10)

fig_heat = go.Figure(data=go.Heatmap(z=date))

fig_heat.update_layout(title="Heatmap 10x10")

fig_heat.show()


# Grafic linii pentru 3 ani consecutivi

luni = ["Ian", "Feb", "Mar", "Apr", "Mai", "Iun", "Iul", "Aug", "Sep", "Oct", "Noi", "Dec"]

vanzari_2022 = np.random.randint(100, 300, 12)
vanzari_2023 = np.random.randint(150, 350, 12)
vanzari_2024 = np.random.randint(200, 400, 12)

fig = go.Figure()

fig.add_trace(go.Scatter(x=luni, y=vanzari_2022, mode="lines", name="2022"))
fig.add_trace(go.Scatter(x=luni, y=vanzari_2023, mode="lines", name="2023"))
fig.add_trace(go.Scatter(x=luni, y=vanzari_2024, mode="lines", name="2024"))

fig.update_layout(title="Vanzari lunare pe 3 ani")

fig.show()

