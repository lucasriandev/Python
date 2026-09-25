import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Creating the dataset
data = pd.DataFrame({
  'size_sqft': [450, 500, 600, 750, 800, 850, 900, 1000, 1100, 1200],
  'floor':     [1, 2, 1, 3, 5, 4, 2, 6, 7, 10],
  'bedrooms':  [1, 1, 1, 2, 2, 2, 2, 3, 3, 3],
  'price':     [1200, 1300, 1450, 1600, 1700, 1750, 1800, 2000, 2150, 2300]
})

df = pd.DataFrame(data)

X = df[['size_sqft', 'floor', 'bedrooms']]
y = df['price']

X_estudo, X_prova, y_estudo, y_prova = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_estudo, y_estudo)

previsao = modelo.predict(X_prova)
print("Oq ele precisa prever!")
print(y_prova.values)

print("Oq ele previu!")
print(previsao)