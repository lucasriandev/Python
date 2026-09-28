#classificação

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier # Mudamos o algoritmo para um Classificador
from sklearn.metrics import accuracy_score      # Ferramenta para calcular a nossa "nota da prova"

# 1. Criando os dados do Banco
dados = {
    'idade': [25, 45, 30, 50, 23, 40, 60, 22, 35, 55],
    'salario': [2500, 8000, 3200, 12000, 1500, 5000, 9000, 1800, 4500, 10000],
    'score_credito': [500, 850, 600, 950, 400, 700, 800, 300, 650, 900],
    'aprovado': [0, 1, 0, 1, 0, 1, 1, 0, 1, 1] # O nosso 'y' (1 = Sim, 0 = Não)
}
df = pd.DataFrame(dados)

# 2. Separando X (perguntas) e y (respostas)
X = df[['idade', 'salario', 'score_credito']]
y = df['aprovado']

# 3. Separando material de Estudo e de Prova (30% para prova)
X_estudo, X_prova, y_estudo, y_prova = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. O modelo "estuda" os dados
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_estudo, y_estudo) 
# Aqui ele descobre regras do tipo: "SE o salário for maior que 4000 E o score maior que 600, APROVA (1)"

# 5. O modelo faz a prova com clientes que ele nunca viu
previsoes = modelo.predict(X_prova)

# 6. Conferindo os resultados
print("O que a máquina previu: ", previsoes)
print("O gabarito real:        ", y_prova.values)

# Calculando a porcentagem de acertos
acuracia = accuracy_score(y_prova, previsoes)
print(f"Taxa de Acerto do Modelo: {acuracia * 100}%")