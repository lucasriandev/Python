import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # Mudou de Classificador para Regressor

# 1. Adaptamos os dados para um problema de Regressão (valores contínuos)
dados = {
    "idade": [22, 25, 47, 52, 46, 56, 27, 32, 38, 41],
    "tempo_no_site": [2, 5, 14, 18, 10, 22, 6, 9, 12, 15],
    "valor_gasto": [15.50, 22.00, 85.00, 110.50, 78.00, 140.00, 28.00, 45.00, 65.00, 72.00] # Novo alvo
}

df = pd.DataFrame(dados)

X = df[["idade", "tempo_no_site"]]
y = df["valor_gasto"]

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

print("\nCorrelação:")
print(X_treino.corr())

# 2. Criando e treinando o modelo de Regressão Linear
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

# 3. Fazendo as previsões
previsoes = modelo.predict(X_teste)

print("\nO que realmente aconteceu (Gabarito):", y_teste.values)
print("O que o modelo previu:            ", previsoes)

# 4. Cálculo dos Resíduos (Aula)
residuos = y_teste - previsoes
print("\nResíduos (Diferença):             ", residuos.values)

# 5. Visualizando os Resíduos com Matplotlib (Aula)
plt.scatter(previsoes, residuos, color='blue')
plt.axhline(y=0, color='red', linestyle='--') # Linha horizontal no zero
plt.xlabel('Valores Previstos (Predicted Values)')
plt.ylabel('Resíduos (Residuals)')
plt.title('Gráfico de Resíduos - Verificando Homocedasticidade')
plt.show()