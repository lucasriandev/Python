import pandas as pd

dados_sujos = {
    "nome": ["Ana", "Bruno", "Carlos", "Ana", "Daniel", None],
    "idade": [28, None, 35, 28, 40, 22],
    "setor": ["Vendas", "TI", "TI", "Vendas", "RH", None],
    "salario": [4500, 5200, 6000, 4500, None, 3000]
}

df = pd.DataFrame(dados_sujos)
print("DADOS ORIGINAIS")
print(df)

# Preenchendo textos vazios com "Desconhecido"
dados_tratados = df["nome"] = df["nome"].fillna("Desconhecido")
print("NOME NULO PREENCHIDO")
print(dados_tratados)

# Preenchendo números vazios com a MÉDIA daquela coluna
media_idade = df["idade"].mean()
print("PREENCHENDO IDADE")
print(media_idade)

media_idade2 = df["idade"].fillna(media_idade)
print("DADOS DE IDADE")
print(media_idade2)

# Preenchendo números vazios com zero
media_idade2 = df["idade"].fillna(0)
print("PREENCHENDO COM 0")
print(media_idade2)
