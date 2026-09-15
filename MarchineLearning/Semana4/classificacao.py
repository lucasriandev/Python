import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

dados = {
    "idade": [22, 25, 47, 52, 46, 56, 27, 32, 38, 41],
    "tempo_no_site": [2, 5, 14, 18, 10, 22, 6, 9, 12, 15],
    "assinou": [0, 0, 1, 1, 1, 1, 0, 0, 1, 1] # 0 = Não, 1 = Sim
}

df = pd.DataFrame(dados)

X = df[["idade", "tempo_no_site"]]
y = df["assinou"]

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_treino, y_treino)

previsoes = modelo.predict(X_teste)

print("O que realmente aconteceu (Gabarito):", y_teste.values)
print("O que o modelo previu:            ", previsoes)

# A Acurácia é a nota da prova: de 0.0 a 1.0 (ou 0% a 100%)
nota = accuracy_score(y_teste, previsoes)
print(f"\nAcurácia do modelo: {nota * 100}%")