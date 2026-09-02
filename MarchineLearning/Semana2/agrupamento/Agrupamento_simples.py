import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Elena", "Felipe"],
    "setor": ["Vendas", "TI", "TI", "RH", "Vendas", "TI"],
    "salario": [4500, 5200, 6000, 3000, 4800, 5500],
    "idade": [28, 22, 35, 40, 29, 25]
}

df = pd.DataFrame(dados)

# A lógica: df.groupby("AgruparPor")["CalcularIsso"].operacao()

# Média salarial por setor
media_salarial = df.groupby("setor")["salario"].mean()
print("--- MÉDIA SALARIAL POR SETOR ---")
print(media_salarial)

# Quantidade de funcionários por setor (count)
qta_funcionarios = df.groupby("setor")["nome"].count()
print("\n--- QUANTIDADE DE FUNCIONÁRIOS ---")
print(qta_funcionarios)

# Transformando o resultado agrupado de volta em uma tabela padrão
tabela_media = df.groupby("setor")["salario"].mean().reset_index()
print("\n--- TABELA FORMATADA COM RESET_INDEX ---")
print(tabela_media)