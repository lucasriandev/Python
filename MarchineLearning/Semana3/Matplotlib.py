#. O Básico com Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_resumo = {
    "setor": ["Vendas", "TI", "RH"],
    "salario_medio": [4650, 5566, 3000]
}

df_resumo = pd.DataFrame(dados_resumo)

#passamos a coluna do eixo x e a coluna do eixo y
plt.bar(df_resumo["setor"], df_resumo["salario_medio"])

# Renderizar o grafico
plt.show()