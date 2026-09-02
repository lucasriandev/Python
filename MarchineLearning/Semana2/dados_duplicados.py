import pandas as pd

dados_sujos = {
    "nome": ["Ana", "Bruno", "Carlos", "Ana", "Daniel", None],
    "idade": [28, None, 35, 28, 40, 22],
    "setor": ["Vendas", "TI", "TI", "Vendas", "RH", None],
    "salario": [4500, 5200, 6000, 4500, None, 3000]
}

df = pd.DataFrame(dados_sujos)
print("Dados originais")
print(df)


print("\n--- LINHAS DUPLICADAS ---")
print(df.duplicated())

df_limpo = df.drop_duplicates()
print("Removendo linhas duplicadas")
print(df_limpo)