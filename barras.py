import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_barras.csv')

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=df, x='categoria', y='vendas_medias', hue='regiao', palette='viridis', ax=ax
)

ax.set_title('Vendas Médias por Categoria e Região', fontsize=14, pad=15)
ax.set_xlabel('Categoria', fontsize=11)
ax.set_ylabel('Vendas Médias (R$)', fontsize=11)
ax.legend(title='Região', frameon=True)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
