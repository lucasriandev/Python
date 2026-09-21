import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dados_empresa = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Elena", "Felipe", "Gabi", "Hugo", "Isabela", "João"],
    "setor": ["Vendas", "TI", "TI", "RH", "Vendas", "TI", "RH", "Vendas", "TI", "Vendas"],
    "salario": [4500, 5200, 6800, 3100, 4800, 5500, 3200, 7200, 6100, 4200],
    "idade": [28, 22, 35, 41, 29, 25, 38, 45, 31, 24],
    "anos_experiencia": [3, 1, 8, 12, 4, 2, 9, 15, 6, 2],
    "satisfacao": [8.5, 7.0, 9.0, 6.0, 7.5, 8.0, 6.5, 8.8, 9.2, 7.0] # Nota de 0 a 10
}

df = pd.DataFrame(dados_empresa)

#Exercicio 1
#plt.bar(df["nome"], df["anos_experiencia"])

#Exercicio 2
#media_salarial = df.groupby("setor")["salario"].mean().reset_index()
#print(media_salarial)

#sns.set_theme('notebook')
#sns.barplot(data=media_salarial, x="setor", y="salario", palette="viridis")
#plt.show()

#Exercicio 3
#sns.scatterplot(data=df, x="idade", y="salario", hue="setor")
#plt.xlabel("idade dos funcionarios", fontsize=12)
#plt.show()

#Exercicio 4
#df_teste = df.copy()
#df_teste.loc[1, "salario"] = np.nan
#df_teste.loc[6, "salario"] = np.nan

#percentual_nulos = df_teste.isnull().mean() * 100
#print(percentual_nulos)

#mediana_preco = df_teste["salario"].median()
#print("Mediana")
#print(mediana_preco)
#df_teste["salario"] = df_teste["salario"].fillna(mediana_preco)
#print("Dados nulos preenchidos com mediana")
#print(df)

#sns.scatterplot(data=df_teste, x="anos_experiencia", y="salario", hue="setor")
#plt.show()

#Exercicio 5
#salario_acima_4500 = df[df["salario"] > 4500]
#print(salario_acima_4500)

#sns.scatterplot(data=salario_acima_4500, x="nome", y="salario", hue="setor")
#plt.show()

#Exercicio 6

#df = df.sort_values(by="idade", ascending=False)
#print(df)

#plt.plot(df["idade"], df["salario"])
#plt.xlabel("idade", fontsize=15)
#plt.ylabel("salario", fontsize=15)
#plt.show()

#Exercicio 7
#sns.histplot(data=df, x="salario", kde=True )
#plt.title("Tendencia de distribuição")
#plt.show()

#Exercicio 8
#sns.barplot(data=df, x="nome", y="salario")
#plt.xticks(rotation=45)
#plt.show()

#Exercicio 9
#sns.scatterplot(data=df, x="anos_experiencia", y="salario", hue="setor", size="satisfacao")
#plt.title("Experiência vs Salário (Tamanho = Satisfação)")
#plt.show()

#Exercicio 10

#media = df.groupby("setor")["satisfacao"].mean()
#print(media)
#plt.savefig("????", dpi=300, bbox_inches="tight")