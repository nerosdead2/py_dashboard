import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_distribuicao.csv')

fig, ax = plt.subplots(figsize=(9, 5))
sns.histplot(data=df, x='idade', bins=15, kde=True, color='#2b5c8f', ax=ax)

ax.set_title('Distribuição de Idade dos Clientes', fontsize=14, pad=15)
ax.set_xlabel('Idade (anos)', fontsize=11)
ax.set_ylabel('Densidade / Contagem', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
