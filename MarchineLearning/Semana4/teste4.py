#classificao 
#codedex
"""
import pandas as pd
import sklearn.datasets
import sklearn.neighbors

data = sklearn.datasets.load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

X = df.drop(columns='target').iloc[:500]
y = df['target'].iloc[:500]

my_model = sklearn.neighbors.KNeighborsClassifier()

my_model.fit(X, y)

row_501 = df.drop(columns='target').iloc[[500]]

prediction = my_model.predict(row_501)

print(prediction)"""

#modelo knn
import pandas as pd
import sklearn.datasets
import sklearn.neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = sklearn.datasets.load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

X = df.drop(columns='target')
y = df['target']

print(df)

X_estudo, X_prova, y_estudo, y_prova =train_test_split(X, y, test_size=0.2, random_state=42)

meuModelo = sklearn.neighbors.KNeighborsClassifier()
meuModelo.fit(X_estudo, y_estudo)

previsao = meuModelo.predict(X_prova)

mediaDeErro = accuracy_score(y_prova, previsao)

print(f"Gabarito {y_prova.values}")

print(f"O modelo estudou {len(X_estudo)} pacientes.")
print(f"O modelo fez a prova com {len(X_prova)} pacientes.")
print(f"Taxa de acerto final: {mediaDeErro * 100:.2f}%")

# Se você quiser simular a previsão de apenas UM paciente específico do teste:
print(f"A previsão para o primeiro paciente da prova foi: {previsao[13]}")