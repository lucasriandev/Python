import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Criando um DataFrame de exemplo
dados = {
    "anos_experiencia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "salario": [1500, 2000, 2800, 3100, 3900, 4500, 5000, 5600, 6100, 6800]
}
df = pd.DataFrame(dados)

# 2. Separando "As Perguntas" (X) e "O Gabarito" (y)
# O scikit-learn espera que X seja uma tabela (DataFrame) e y seja uma série/coluna única.
X = df[["anos_experiencia"]] 
y = df["salario"]

# 3. Dividindo em Treino e Teste (80% treino, 20% teste)
# O random_state garante que o sorteio seja sempre o mesmo toda vez que rodar o código.
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Criando e Treinando o Modelo (A Inteligência Artificial nascendo aqui)
modelo = LinearRegression() # Criamos o robô vazio
modelo.fit(X_treino, y_treino) # Damos os livros de estudo (treino) para ele aprender

# 5. Colocando o Modelo à Prova
previsoes = modelo.predict(X_teste)

# 6. Avaliando o resultado
print("Gabarito Real (Dados de Teste):")
print(y_teste.values)

print("\nO que o modelo previu:")
print(previsoes)

# Calculando a margem de erro (em Reais, o quanto ele errou para mais ou para menos em média)
erro_medio = mean_absolute_error(y_teste, previsoes)
print(f"\nO modelo está errando o salário em média por: R$ {erro_medio:.2f}")