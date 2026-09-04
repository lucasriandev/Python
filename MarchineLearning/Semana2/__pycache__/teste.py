import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Elena", "Felipe"],
    "setor": ["Vendas", "TI", "TI", "RH", "Vendas", "TI"],
    "salario": [4500, 5200, 6000, 3000, 4800, 5500],
    "idade": [28, 22, 35, 40, 29, 25],
}

df = pd.DataFrame(dados)

print("Dados originais")
print(df)

dados_tratados = df[(df["setor"] == "Vendas") | (df["salario"] > 5000)] 
print("exercicio 1")
print(dados_tratados)

df["bonus"] = df["salario"] * 0.15
print("Exercicio 2 criando bonus")
print(df)

df["remuneracao_total"] = df["salario"] + df["bonus"]
print("Exercicio 2 somando bonus")
print(df)

dados_repetidos = {
    "cliente": ["Loja A", "Loja B", "Loja A", "Loja C", "Loja B"],
    "cidade": ["SP", "RJ", "SP", "MG", "PR"],
    "vendas": [1000, 1500, 1000, 700, 1200],
}
df_clientes = pd.DataFrame(dados_repetidos)

print("Dados Exercicio 3")
print(df_clientes)
print("Dados duplicados")
print(df_clientes.duplicated())

df_limpo = df_clientes.drop_duplicates(subset=["cliente"])
print("Dados duplicados limpos")
print(df_limpo)

dados_incompletos = {
    "produto": ["Teclado", "Mouse", "Monitor", "Headset", "Cabo HDMI"],
    "preco": [150.0, None, 850.0, 200.0, None],
    "estoque": [20, 50, None, None, 100],
}
df_estoque = pd.DataFrame(dados_incompletos)

print("Exercicio 4")
print(df_estoque)

print("Quantidade de vazios!")
print(df_estoque.isnull().mean() * 100)

print("Exercicio 5")
df_estoque["preco"] = df_estoque["preco"].fillna(0)
df_estoque["estoque"] = df_estoque['estoque'].fillna(0)
print(df_estoque)

print("Exercicio 6")
novo_data = df_estoque.dropna(subset=["preco"])
print(" Nova tabela")
print(novo_data)

print("Exercicio 7")
agrupamento = df.groupby("setor")["salario"].min().reset_index()
print(agrupamento)

print("Exercicio 8")
resumo_completo = df.groupby("setor").agg({
    "salario": ["mean", "sum"],
    "idade": ["min", "max"],
    "nome": ["count"]
}).reset_index()

print("\n--- RESUMO COMPLETO POR SETOR ---")
print(resumo_completo)