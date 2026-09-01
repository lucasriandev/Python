import pandas as pd

#importando arquivos cvs
df_vendas = pd.read_csv("vendas.csv")
df_vendas_br = pd.read_csv("vendas_brasil.csv", sep=";")

#arquivos excel
df_planilhas = pd.read_excel("relatorio_financeiro.xlsx")
df_aba2 = pd.read_excel("relatorio_finaceiro.xlsx", sheet_name="Aba 2")

# 1. df.shape -> Retorna (linhas, colunas). 
# Não tem parênteses no final porque é um atributo, não uma função (como o .length do JS)
print(df_vendas.shape) 

# 2. df.info() -> Mostra o nome de todas as colunas, se tem dados faltando (nulos) 
# e o tipo de dado (texto, número inteiro, decimal, etc).
print(df_vendas.info())

# 3. df.describe() -> Gera estatísticas automáticas das colunas numéricas 
# (média, valor mínimo, máximo, etc)
print(df_vendas.describe())

#exportando arquivos novos csv
df_vendas.to_csv("dados_tratados", index=False)

#exportando excel
df_vendas.to_excel("dados_novos", index=False)