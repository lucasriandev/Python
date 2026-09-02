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

print("\n--- VALORES VAZIOS POR COLUNA ---")
# Retorna a quantidade de células vazias por coluna
print(df.isnull().sum())

# Apaga QUALQUER linha que tenha pelo menos um valor NaN
df_sem_nulos = df.dropna()
print("VALORES NULOS APAGADOS")
print(df_sem_nulos)

# Apaga a linha APENAS SE a coluna 'salario' estiver vazia
df_salario_limpo = df.dropna(subset=["salario"])
print("Apaga coluna que tem algum valor nulo (daniel)")
print(df_salario_limpo)


