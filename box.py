import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_boxplot.csv')

fig, ax = plt.subplots(figsize=(9, 6))
sns.boxplot(
    data=df,
    x='departamento',
    y='salario',
    hue='departamento',
    palette='Set2',
    legend=False,
    width=0.5,
    ax=ax,
)

ax.set_title('Distribuição Salarial por Departamento (Boxplot)', fontsize=14, pad=15)
ax.set_xlabel('Departamento', fontsize=11)
ax.set_ylabel('Salário (R$)', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
