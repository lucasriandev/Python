import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

dados = {
    "idade" : [21,22,23],
    "salario": [1000, 2000, 3000]
}

df = pd.DataFrame(dados)

X = df[["idade"]]
y = df["salario"]

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

previsao = modelo.predict(X_teste)

print("\nO que o modelo previu:")
print(previsao)