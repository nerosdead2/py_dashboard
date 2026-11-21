import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_dispersao.csv')

fig, ax = plt.subplots(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x='altura_cm',
    y='peso_kg',
    hue='sexo',
    style='sexo',
    alpha=0.8,
    s=60,
    ax=ax,
)

ax.set_title('Gráfico de Dispersão: Altura vs. Peso por Sexo', fontsize=14, pad=15)
ax.set_xlabel('Altura (cm)', fontsize=11)
ax.set_ylabel('Peso (kg)', fontsize=11)
ax.legend(title='Sexo', frameon=True)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
