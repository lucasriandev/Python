import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


dados = dados = {
    "anos_experiencia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "salario": [1500, 2000, 2800, 3100, 3900, 4500, 5000, 5600, 6100, 6800]
}

df = pd.DataFrame(dados)

# 2. Separando "As Perguntas" (X) e "O Gabarito" (y)
X = df[["anos_experiencia"]]
y = df["salario"]

# 3. Dividindo em Treino e Teste (80% treino, 20% teste)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
print("Dados separados em Treino e Teste!")

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)
print("Robo treinado!")

previsoes = modelo.predict(X_teste)

print("Gabarito Real (Dados de Teste):")
print(y_teste.values)

print("\nO que o modelo previu:")
print(previsoes)