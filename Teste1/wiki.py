import pandas as pd

url = "http://localhost:3000/animes"

# 1. Carrega os dados da API
df = pd.read_json(url)

# 2. Pega os dicionários que estão dentro da coluna "dados"
df = pd.json_normalize(df["dados"])

# 3. Mostra informações
df.info()

print("Informações")
print(df.head())

# 4. Procura Naruto
achando_naruto = df[df["nome"] == "Naruto"]

print("Achando Naruto:")
print(achando_naruto)