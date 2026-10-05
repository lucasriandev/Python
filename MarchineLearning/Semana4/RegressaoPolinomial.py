import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Os mesmos dados base da regressão anterior
dados = {
    "idade": [22, 25, 47, 52, 46, 56, 27, 32, 38, 41],
    "tempo_no_site": [2, 5, 14, 18, 10, 22, 6, 9, 12, 15],
    "valor_gasto": [15.50, 22.00, 85.00, 110.50, 78.00, 140.00, 28.00, 45.00, 65.00, 72.00]
}

df = pd.DataFrame(dados)

# ==============================================================
# 2. APLICANDO A REGRESSÃO POLINOMIAL (Adicionando os novos termos)
# ==============================================================
# Criando novas colunas elevando a idade ao quadrado e ao cubo
df["idade_quadrada"] = df["idade"] ** 2
df["idade_cubica"] = df["idade"] ** 3

# Imprimindo o DataFrame para confirmar que foram adicionadas (como a instrução pediu)
print("DataFrame com as novas características (features) polinomiais:\n")
print(df)
print("-" * 50)

# 3. Atualizamos o 'X' para incluir as novas colunas curvadas
X = df[["idade", "tempo_no_site", "idade_quadrada", "idade_cubica"]]
y = df["valor_gasto"]

# 4. Dividindo e treinando (Repare que o modelo continua sendo o LinearRegression!)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

# 5. Fazendo as previsões
previsoes = modelo.predict(X_teste)

print("\nO que realmente aconteceu (Gabarito):", y_teste.values)
print("O que o modelo previu:            ", previsoes.round(2))