import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_linhas.csv')
df['data'] = pd.to_datetime(df['data'])

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=df, x='data', y='vendas', hue='loja', marker='o', markersize=4, ax=ax)

ax.set_title('Evolução de Vendas por Loja (Gráfico de Linhas)', fontsize=14, pad=15)
ax.set_xlabel('Data', fontsize=11)
ax.set_ylabel('Vendas (R$)', fontsize=11)
ax.legend(title='Loja', frameon=True)
ax.grid(True, linestyle='--', alpha=0.5)

fig.autofmt_xdate()
plt.tight_layout()
plt.show()
