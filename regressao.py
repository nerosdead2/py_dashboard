import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_regressao.csv')

fig, ax = plt.subplots(figsize=(9, 6))
sns.regplot(
    data=df,
    x='renda_mensal',
    y='gasto_mensal',
    scatter_kws={'alpha': 0.7, 'color': '#1f77b4'},
    line_kws={'color': '#d62728', 'linewidth': 2},
    ax=ax,
)

ax.set_title('Regressão Linear: Renda Mensal vs. Gasto Mensal', fontsize=14, pad=15)
ax.set_xlabel('Renda Mensal (R$)', fontsize=11)
ax.set_ylabel('Gasto Mensal (R$)', fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
