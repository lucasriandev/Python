import pandas as pd
import sklearn.datasets

data = sklearn.datasets.load_breast_cancer()
print(data)

df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target
print(df)