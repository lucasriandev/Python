import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Elena", "Felipe"],
    "setor": ["Vendas", "TI", "TI", "RH", "Vendas", "TI"],
    "salario": [4500, 5200, 6000, 3000, 4800, 5500],
    "idade": [28, 22, 35, 40, 29, 25],
}

df = pd.DataFrame(dados)

print("\nEXERCICIO 1")
filtro = df[(df["setor"] == "Vendas") | (df["salario"] > 5000)]
print(filtro)

print("\nEXERCICIO 2")
# 1. Cria a coluna bonus (15% do salário)
df["bonus"] = df["salario"] * 0.15

df["remuneracao_total"] = df["bonus"] + df["bonus"]

print(df[["nome", "salario", "bonus", "remuneracao_total"]])

dados_repetidos = {
    "cliente": ["Loja A", "Loja B", "Loja A", "Loja C", "Loja B"],
    "cidade": ["SP", "RJ", "SP", "MG", "PR"],
    "vendas": [1000, 1500, 1000, 700, 1200],
}

df_clientes = pd.DataFrame(dados_repetidos)

print("\nEXERCICIO 3")

total_duplicadas = df_clientes.duplicated().sum()
print(f"Total de linhas idênticas duplicadas: {total_duplicadas}")

df_clientes_unicos = df_clientes.drop_duplicates(subset=["cliente"])
print("\nClientes unicos:")
print(df_clientes_unicos)

dados_incompletos = {
    "produto": ["Teclado", "Mouse", "Monitor", "Headset", "Cabo HDMI"],
    "preco": [150.0, None, 850.0, 200.0, None],
    "estoque": [20, 50, None, None, 100],
}

df_estoque = pd.DataFrame(dados_incompletos)

print("\nEXERCICIO 4")

percentual_nulos = df_estoque.isnull().mean() * 100
print("Porcentagem de nulos por coluna (%):")
print(percentual_nulos)

print("\nEXERCICIO 5")
mediana_preco = df_estoque["preco"].median()
df_estoque["preco"] = df_estoque["preco"].fillna(mediana_preco)

print(f"\n{df_estoque}")

df_estoque["estoque"] = df_estoque["estoque"].fillna(0)
print(df_estoque)

print("\nEXERCICIO 6")
df_estoque_original = pd.DataFrame(dados_incompletos)

df_preco_valido = df_estoque_original.dropna(subset=["preco"])
print(df_preco_valido)

print("\nEXERCICIO 7")
salarios_extremos = (df.groupby("setor")["salario"].agg(["min", "max"]).reset_index())
print(salarios_extremos)

print("\nEXERCICIO 8")
resumo_avançado = df.groupby("setor").agg({
    "salario": ["sum", "mean"],
    "idade": ["min", "max"],
    "nome": ["count"]
}).reset_index()

print(resumo_avançado)

print("\nEXERCICIO 9")
# Leitura configurando o separador e o encoding correto
df_produtos = pd.read_csv("produtos_europa.csv", sep=";", encoding="latin1")

print("\nEXERCICIO 10")
# 1. Exportando para CSV sem o índice numérico
resumo_avançado.to_csv("resumo_setores.csv", index=False)

# 2. Exportando para Excel com nome específico na aba
resumo_avançado.to_excel("relatorio_final.xlsx", sheet_name="Consolidado", index=False)

print("Arquivos exportados com sucesso!")