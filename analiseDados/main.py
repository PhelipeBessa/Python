#pip install pandas
# pip install plotly_express
import pandas as pd
import plotly_express as px

dados = pd.read_excel("vendas.xlsx")

# Análise Explorativa
dados.head() # 5 primeiras linhas
dados.tail() # últimas linhas
dados.shape() # total de linhas e colunas

# Estatítica
dados.describe()

# Análises
dados.loja.value_counts() # Total de pedidos por Loja
dados.forma_pagamento.value_counts() # Total de pedidos por forma de pagamento
dados.tamanho.value_counts() # Total de pedidos por copo

# Faturamento
dados.groupby("loja").sum() # Faturamento por loja
dados.groupby("loja").mean() # Ticket médio por loja
dados_agrupados_estado_loja = dados.groupby(["estado", "loja"]).sum()
dados_agrupados_estado_loja.to_excel("Faturamento por estado.xlsx") # Exportar por e-mail

# Visualização de Dados
px.histogram(dados, x='loja') # Gráfico
px.histogram(dados, x='loja', color='estado')
px.histogram(dados, x='loja', color='estado', text_auto=True)
px.histogram(dados, x='loja', y='preco', color='estado', text_auto=True)
px.histogram(dados, x='loja', y='preco', color='forma_pagamento', text_auto=True)
grafico = px.histogram(dados, x='loja', y='preco', color='forma_pagamento', text_auto=True)
grafico.show()
grafico.write_html("faturamento_loja.html") # Exportar para HTML

#Vetores
colunas =["loja", "cidade", "estado", "regiao", "tamanho", "local_consumo", "forma_pagamento"]
for coluna in colunas:
    grafico = px.histogram(dados, x=coluna, y='preco', color='forma_pagamento', text_auto=True)
    grafico.show()
    grafico.write_html(f"grafico - {coluna}.html") # Gerar gráfico em html cada um com o nome gravado no vetor