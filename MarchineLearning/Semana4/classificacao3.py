#base de dados com 1000

import pandas as pd
import numpy as np  # Biblioteca para gerar os dados aleatórios
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. GERANDO 1000 LINHAS DE DADOS FICTÍCIOS
np.random.seed(42) # Trava o gerador aleatório para o resultado ser igual toda vez que rodar
quantidade = 1000

# Sorteando dados aleatórios para os 1000 clientes
idades = np.random.randint(18, 70, quantidade)
salarios = np.random.randint(1500, 15000, quantidade)
scores_credito = np.random.randint(300, 950, quantidade)

# Criando a "Regra do Banco" para aprovar (1) ou reprovar (0)
aprovado = []
for i in range(quantidade):
    # Regra lógica: aprova se o salário > 4000 E score > 600, OU se o salário > 8000
    if (salarios[i] > 4000 and scores_credito[i] > 600) or salarios[i] > 8000:
        aprovado.append(1)
    else:
        aprovado.append(0)

# Adicionando um "ruído" (bagunçando 50 resultados de propósito)
# Isso simula o mundo real, onde clientes bons às vezes são reprovados e vice-versa
for i in range(50):
    cliente_aleatorio = np.random.randint(0, quantidade)
    aprovado[cliente_aleatorio] = np.random.choice([0, 1])

# Montando a tabela final
df = pd.DataFrame({
    'idade': idades,
    'salario': salarios,
    'score_credito': scores_credito,
    'aprovado': aprovado
})

print(f"Base criada com sucesso! Analisando {len(df)} clientes...\n")


# 2. O MESMO CÓDIGO DE MACHINE LEARNING (AGORA COM DADOS ROBUSTOS)
X = df[['idade', 'salario', 'score_credito']]
y = df['aprovado']

# Separando 20% para prova (A prova agora terá 200 clientes)
X_estudo, X_prova, y_estudo, y_prova = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_estudo, y_estudo)

previsoes = modelo.predict(X_prova)
acuracia = accuracy_score(y_prova, previsoes)

print(f"O modelo estudou {len(X_estudo)} casos.")
print(f"O modelo fez uma prova com {len(X_prova)} casos.")
print(f"Taxa de Acerto: {acuracia * 100:.2f}%")