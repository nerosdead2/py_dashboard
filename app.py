import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title='Dashboard de Análise de Dados',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded',
)

with st.sidebar:
    st.markdown('Nome: Caio Antunes Guedes Alves da Silva')
    st.markdown('Número: 08')
    st.markdown('Turma: 3D1')
    st.divider()

st.title(' Dashboard de Visualização e Análise de Dados')
st.markdown('Painel consolidado com os 9 conjuntos de dados analisados.')
st.divider()


@st.cache_data
def carregar_csv(caminho: str) -> pd.DataFrame:
    return pd.read_csv(caminho)


col1, col2, col3 = st.columns(3, gap='medium')

with col1:
    st.subheader('1. Vendas por Categoria e Região')
    df_barras = carregar_csv('dados_barras.csv')
    fig1, ax1 = plt.subplots(figsize=(6, 4.5))
    sns.barplot(
        data=df_barras,
        x='categoria',
        y='vendas_medias',
        hue='regiao',
        palette='viridis',
        ax=ax1,
    )
    ax1.set_xlabel('Categoria')
    ax1.set_ylabel('Vendas Médias (R$)')
    ax1.legend(title='Região', fontsize=8, title_fontsize=9)
    ax1.tick_params(axis='x', rotation=15)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)
    st.info(
        '**Análise:** A região Oeste apresenta as maiores vendas médias em quase '
        'todas as categorias, com destaque para Livros (R$ 284,18) e Brinquedos '
        '(R$ 281,17), enquanto Eletrônicos lidera na região Leste.'
    )

with col2:
    st.subheader('2. Distribuição Salarial (Boxplot)')
    df_box = carregar_csv('dados_boxplot.csv')
    fig2, ax2 = plt.subplots(figsize=(6, 4.5))
    sns.boxplot(
        data=df_box,
        x='departamento',
        y='salario',
        hue='departamento',
        palette='Set2',
        legend=False,
        width=0.5,
        ax=ax2,
    )
    ax2.set_xlabel('Departamento')
    ax2.set_ylabel('Salário (R$)')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)
    st.info(
        '**Análise:** TI e Vendas possuem as maiores medianas e dispersões salariais. '
        'Todos os quatro departamentos apresentam *outliers* superiores bem definidos, '
        'indicando cargos de liderança ou especialização com remuneração acima da média.'
    )

with col3:
    st.subheader('3. Altura vs. Peso por Sexo')
    df_disp = carregar_csv('dados_dispersao.csv')
    fig3, ax3 = plt.subplots(figsize=(6, 4.5))
    sns.scatterplot(
        data=df_disp,
        x='altura_cm',
        y='peso_kg',
        hue='sexo',
        style='sexo',
        alpha=0.8,
        s=50,
        ax=ax3,
    )
    ax3.set_xlabel('Altura (cm)')
    ax3.set_ylabel('Peso (kg)')
    ax3.legend(title='Sexo', fontsize=8, title_fontsize=9)
    ax3.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)
    st.info(
        '**Análise:** Observa-se uma forte correlação linear positiva entre altura e peso '
        'para ambos os sexos: conforme a estatura aumenta, o peso acompanha proporcionalmente, '
        'sem separação rígida entre os dois grupos.'
    )

st.divider()

col4, col5, col6 = st.columns(3, gap='medium')

with col4:
    st.subheader('4. Distribuição Etária dos Clientes')
    df_dist = carregar_csv('dados_distribuicao.csv')
    fig4, ax4 = plt.subplots(figsize=(6, 4.5))
    sns.histplot(data=df_dist, x='idade', bins=15, kde=True, color='#2b5c8f', ax=ax4)
    ax4.set_xlabel('Idade (anos)')
    ax4.set_ylabel('Contagem')
    ax4.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig4)
    plt.close(fig4)
    st.info(
        '**Análise:** A curva de densidade revela uma distribuição bimodal clara, '
        'com dois públicos distintos: um grande agrupamento de jovens adultos (20 a 30 anos) '
        'e um segundo grupo maduro concentrado entre 43 e 55 anos.'
    )

with col5:
    st.subheader('5. Frequência de Atendimentos')
    df_freq = carregar_csv('dados_frequencia.csv')
    ordem = df_freq['tipo_atendimento'].value_counts().index
    fig5, ax5 = plt.subplots(figsize=(6, 4.5))
    sns.countplot(
        data=df_freq,
        x='tipo_atendimento',
        order=ordem,
        hue='tipo_atendimento',
        palette='coolwarm',
        legend=False,
        ax=ax5,
    )
    for container in ax5.containers:
        ax5.bar_label(container, padding=2, fontsize=9, fontweight='bold')
    ax5.set_ylim(0, df_freq['tipo_atendimento'].value_counts().max() * 1.15)
    ax5.set_xlabel('Tipo de Atendimento')
    ax5.set_ylabel('Frequência')
    ax5.tick_params(axis='x', rotation=15)
    ax5.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig5)
    plt.close(fig5)
    st.info(
        '**Análise:** Chamados de "Dúvida" e "Reclamação" representam a maior parte '
        'da demanda do suporte, enquanto "Cancelamento" e "Elogio" aparecem em menor volume, '
        'sugerindo oportunidades de melhoria na documentação de autoatendimento.'
    )

with col6:
    st.subheader('6. Movimento de Clientes (Heatmap)')
    df_heat = carregar_csv('dados_heatmap.csv')
    ordem_dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    matriz = df_heat.pivot(
        index='dia_semana', columns='horario', values='movimento_clientes'
    ).reindex(ordem_dias)
    fig6, ax6 = plt.subplots(figsize=(6, 4.5))
    sns.heatmap(
        matriz,
        annot=True,
        fmt='d',
        cmap='YlOrRd',
        linewidths=0.5,
        annot_kws={'size': 8},
        ax=ax6,
    )
    ax6.set_xlabel('Horário')
    ax6.set_ylabel('Dia da Semana')
    plt.tight_layout()
    st.pyplot(fig6)
    plt.close(fig6)
    st.info(
        '**Análise:** O fluxo de clientes intensifica-se expressivamente no fim de semana, '
        'atingindo picos no Domingo às 12h (199) e às 18h (197), e no Sábado às 20h (164). '
        'Nos dias úteis, o movimento é mais moderado.'
    )

st.divider()

col7, col8, col9 = st.columns(3, gap='medium')

with col7:
    st.subheader('7. Evolução de Vendas por Loja')
    df_linhas = carregar_csv('dados_linhas.csv')
    df_linhas['data'] = pd.to_datetime(df_linhas['data'])
    fig7, ax7 = plt.subplots(figsize=(6, 4.5))
    sns.lineplot(
        data=df_linhas,
        x='data',
        y='vendas',
        hue='loja',
        marker='o',
        markersize=3,
        ax=ax7,
    )
    ax7.set_xlabel('Data')
    ax7.set_ylabel('Vendas (R$)')
    ax7.legend(title='Loja', fontsize=8, title_fontsize=9)
    ax7.tick_params(axis='x', rotation=30)
    ax7.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig7)
    plt.close(fig7)
    st.info(
        '**Análise:** Ambas as lojas apresentam tendência consistente de crescimento '
        'ao longo do 1º trimestre de 2026, saltando do patamar de ~R$ 100 em janeiro '
        'para valores próximos de R$ 250 ao final de março.'
    )

with col8:
    st.subheader('8. Faturamento por Canal (Pizza)')
    df_pizza = carregar_csv('dados_pizza.csv')
    fig8, ax8 = plt.subplots(figsize=(6, 4.5))
    cores = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']
    ax8.pie(
        df_pizza['faturamento'],
        labels=df_pizza['canal_venda'],
        autopct='%1.1f%%',
        startangle=90,
        colors=cores,
        textprops={'fontsize': 9},
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.2},
    )
    ax8.axis('equal')
    plt.tight_layout()
    st.pyplot(fig8)
    plt.close(fig8)
    st.info(
        '**Análise:** O canal digital (Site + Aplicativo) concentra 55% de todo o '
        'faturamento (37,5% no Site e 17,5% no App), seguido pela Loja Física com 26,7%, '
        'evidenciando a predominância das vendas online.'
    )

with col9:
    st.subheader('9. Regressão: Renda vs. Gasto')
    df_reg = carregar_csv('dados_regressao.csv')
    fig9, ax9 = plt.subplots(figsize=(6, 4.5))
    sns.regplot(
        data=df_reg,
        x='renda_mensal',
        y='gasto_mensal',
        scatter_kws={'alpha': 0.65, 'color': '#1f77b4', 's': 25},
        line_kws={'color': '#d62728', 'linewidth': 2},
        ax=ax9,
    )
    ax9.set_xlabel('Renda Mensal (R$)')
    ax9.set_ylabel('Gasto Mensal (R$)')
    ax9.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig9)
    plt.close(fig9)
    st.info(
        '**Análise:** Existe uma relação linear altamente previsível entre renda e gasto mensal: '
        'os pontos seguem de perto a reta de regressão, demonstrando que o consumo cresce '
        'em torno de 55% a 60% da renda adicional.'
    )
