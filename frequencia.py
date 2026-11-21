import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_frequencia.csv')
ordem = df['tipo_atendimento'].value_counts().index

fig, ax = plt.subplots(figsize=(9, 5))
sns.countplot(
    data=df,
    x='tipo_atendimento',
    order=ordem,
    hue='tipo_atendimento',
    palette='coolwarm',
    legend=False,
    ax=ax,
)

for container in ax.containers:
    ax.bar_label(container, padding=3, fontweight='bold')

ax.set_ylim(0, df['tipo_atendimento'].value_counts().max() * 1.12)
ax.set_title('Frequência de Chamados por Tipo de Atendimento', fontsize=14, pad=15)
ax.set_xlabel('Tipo de Atendimento', fontsize=11)
ax.set_ylabel('Frequência Absoluta', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
