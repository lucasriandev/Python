import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Elena", "Felipe"],
    "setor": ["Vendas", "TI", "TI", "RH", "Vendas", "TI"],
    "salario": [4500, 5200, 6000, 3000, 4800, 5500],
    "idade": [28, 22, 35, 40, 29, 25]
}

df = pd.DataFrame(dados)

resumo_completo = df.groupby("setor").agg({
    "salario": ["mean", "sum", "max"],
    "idade": ["mean"],
    "nome": ["count"]
}).reset_index()

print("\n--- RESUMO COMPLETO POR SETOR ---")
print(resumo_completo)
