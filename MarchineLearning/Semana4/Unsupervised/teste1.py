import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Criando a tabela de dados original
data = {
  'City': [
    'Seattle', 'Boston', 'San Francisco', 'Chicago', 'Minneapolis',
    'Denver', 'Miami', 'Houston', 'Phoenix', 'Las Vegas'
  ],
  'Average Temperature': [
    60, 63, 68, 65, 55,
    70, 85, 88, 90, 95
  ],
  'Average Humidity': [
    80, 70, 75, 60, 50,
    40, 85, 90, 20, 15
  ]
}

df = pd.DataFrame(data)

# 2. Separando apenas os números (X) para o modelo estudar
X = df[['Average Temperature', 'Average Humidity']]

# 3. Criando o modelo e forçando a divisão em 3 grupos
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# 4. Salvando os crachás (0, 1 ou 2) em uma nova coluna na nossa tabela
df['Grupo'] = model.labels_

print("Tabela completa com a nova coluna de Grupos:")
print(df)
print("\n" + "-"*40 + "\n")

# 5. Testando em qual grupo uma cidade nova vai cair
new_city = [[50, 68]]  # Formato exigido pelo scikit-learn (lista dentro de lista)
new_city_cluster = model.predict(new_city)
print(f"A nova cidade (Temp: 50, Umidade: 68) foi classificada no Grupo: {new_city_cluster[0]}")

# ==========================================
# 6. CRIANDO O GRÁFICO
# ==========================================

# Aumenta um pouco o tamanho da janela do gráfico para não ficar espremido
plt.figure(figsize=(10, 6))

# Desenha as bolinhas coloridas
sns.scatterplot(
    data=df,
    x='Average Temperature',
    y='Average Humidity',
    hue='Grupo',
    palette='Set1',
    s=150 # Tamanho da bolinha
)

# Passa linha por linha da tabela escrevendo o nome da cidade perto da bolinha
for index, linha in df.iterrows():
    plt.text(linha['Average Temperature'] + 0.5, linha['Average Humidity'], linha['City'])

# Coloca um título e exibe a janela na sua tela
plt.title('Agrupamento de Cidades por Clima (K-Means)')
plt.show()