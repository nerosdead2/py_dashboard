import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_heatmap.csv')

ordem_dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
matriz = df.pivot(
    index='dia_semana', columns='horario', values='movimento_clientes'
).reindex(ordem_dias)

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(matriz, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5, ax=ax)

ax.set_title('Mapa de Calor: Movimento de Clientes por Dia e Horário', fontsize=14, pad=15)
ax.set_xlabel('Horário', fontsize=11)
ax.set_ylabel('Dia da Semana', fontsize=11)

plt.tight_layout()
plt.show()
