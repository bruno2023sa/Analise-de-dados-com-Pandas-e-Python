# -*- coding: utf-8 -*-
"""Aula8-Analise_Exploratoria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S0gXMp6Ucd8etzD7CJUdnWYICwXrr071
"""

# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# Upload do arquivo
from google.colab import files
arq = files.upload()

# Criando nosso DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

# Visualizando as 5 primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape

# Verificando os tipos de dados
df.dtypes

# Qual foi a Receita total?
df["Valor Venda"].sum()

# Criando a coluna "Valor Custo"
df["Valor Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

df.head(1)

# Qual o custo Total?
round(df["Valor Custo"].sum(), 2)

# Agora que temos a receita e custo e o total, podemos achar o Lucro Total
# Vamos criar uma coluna de Lucro que será Receita - Custo
df["Lucro"] = df["Valor Venda"] - df["Valor Custo"]

df.head(1)

# Qual é o Lucro Total?
round(df["Lucro"].sum(), 2)

# Criando uma coluna com total de dias para enviar o produto
df["Tempo Envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

"""##### **Agora, queremos saber a média do tempo de envio para cada Marca, e para isso precisamos transformar a coluna tempo_envio em numéria**"""

# Extraindo apenas os dias
df["Tempo Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

# Verificando o tipo de coluna "Tempo Envio"
df["Tempo Envio"].dtype

# Média do tempo de envio por Marca
df.groupby("Marca")["Tempo Envio"].mean()

"""##### **Missing Values**"""

# Verificando se temos dados faltantes
df.isnull().sum()

"""##### **E se quisermos saber o Lucro por Ano e Por Marca?**"""

# Vamos agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format # para formar o código acima

# Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
lucro_ano

# Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Gráfico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro X Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()

# Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel(Mês)
plt.ylabel("Lucro");

df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");

df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");

df["Tempo Envio"].describe()

# gráfico de Bosplot
plt.boxplot(df["Tempo Envio"]);

# Histograma
plt.hist(df["Tempo Envio"]);

# Tempo mínimo de envio
df["Tempo Envio"].min()

# Tempo máximo de envio
df["Tempo Envio"].max()

# Identificando o Outlier
df[df["Tempo Envio"] == 20]

df.to_csv("df_vendas_novo.csv", index=False)

