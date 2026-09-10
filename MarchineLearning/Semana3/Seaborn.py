import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_resumo = {
    "setor": ["Vendas", "TI", "RH"],
    "salario_medio": [4650, 5566, 3000]
}
df_resumo = pd.DataFrame(dados_resumo)

#data = meu dataframe | x = nome da coluna horizontal | y = nome da coluna vertical
#sns.barplot(data=df_resumo, x="setor", y="salario_medio")

sns.set_theme(style="whitegrid")
sns.scatterplot(data=df_resumo, x="setor", y="salario_medio", palette="viridis")

plt.title("Media salarial por setor", fontsize=16)
plt.xlabel("Setores da Empresa", fontsize=12)
plt.ylabel("Salario em R$", fontsize=12)

plt.show()