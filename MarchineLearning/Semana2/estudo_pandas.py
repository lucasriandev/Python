import pandas as pd
import numpy as np

dados = {
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [28, 22, 35],
    "setor": ["Vendas", "TI", "TI"],
    "salario": [4500, 5200, 6000]
}

df = pd.DataFrame(dados)

#funcionarios_ti = df[df["setor"] == "TI"]
#print(funcionarios_ti)

#filtro_salario = df[(df["setor"] == "TI") & (df["salario"] > 5500)]
#print(filtro_salario)

#criando nova tabela com aumento de salario
df["salario_com_aumento"] = df["salario"] * 1.10
print(df)

media_salarial = df["salario"].mean()
print(f"A media salarial é R$ {media_salarial}")

