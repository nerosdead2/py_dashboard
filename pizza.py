import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dados_pizza.csv')

fig, ax = plt.subplots(figsize=(8, 8))
cores = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']

ax.pie(
    df['faturamento'],
    labels=df['canal_venda'],
    autopct='%1.1f%%',
    startangle=90,
    colors=cores,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
)

ax.set_title('Participação no Faturamento por Canal de Venda', fontsize=14, pad=15)
ax.axis('equal')

plt.tight_layout()
plt.show()
