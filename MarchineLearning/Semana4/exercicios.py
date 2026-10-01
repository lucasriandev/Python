import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.DataFrame({
    'tamanho': [1000, 1500, 2000, 2500],
    'preco': [200, 250, 300, 350]
})

df = pd.DataFrame(data)
print(data)

X = df[["tamanho"]]
y = df['preco']

X_prova, X_estudo, y_prova, y_estudo = train_test_split(X, y, test_size=0.50, random_state=42)

modelo = LinearRegression()
modelo.fit(X_estudo, y_estudo)

previsao = modelo.predict(X_prova)
print("Oq ele precisa prever!")
print(y_prova.values)

print("Oq ele previu!")
print(previsao)

