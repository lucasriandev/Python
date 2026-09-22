import pandas as pd
from sklearn import preprocessing

data = {
"empregador": ["Corpo de Bombeiros", "Secretaria da Saúde", "Policia Civil"],
"idade": [44,50,80,],
"remuneracao": [7200, 9000, 5000]
}

df = pd.DataFrame(data)

label_encoder = preprocessing.LabelEncoder()
df["empregador"] = label_encoder.fit_transform(df["empregador"])
print(df)