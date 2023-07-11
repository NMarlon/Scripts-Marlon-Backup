import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import r2_score

"""
# Importar a coluna 'XC1' como um array
coluna_xc1 = pd.read_csv(caminho_arquivo, usecols=['EC1']).values.flatten()

# Exibir o array
print(coluna_xc1)



# Dados de treinamento
X_train = np.array([[1], [2], [3], [4], [5]])  # Valores de entrada
y_train = np.array([2, 4, 6, 8, 10])  # Valores de saída correspondentes

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Valor a ser previsto
X_test = np.array([[6]])  # Valor de entrada para previsão

# Fazer a previsão
y_pred = model.predict(X_test)

# Imprimir o resultado da previsão
print("Valor previsto:", y_pred[0])

"""


import pandas as pd
from sklearn.linear_model import LinearRegression

test_mode=False

if test_mode:
    
    # Carregar o arquivo CSV
    df = pd.read_csv('./t2.csv')#train.csv')
    
    # Índices das colunas de entrada (outras colunas)
    colunas_entrada_indices = list(range(1, 2))  # Índices das colunas de "0" a "31" (A:AF)
else:
    df = pd.read_csv('./train.csv')
    # Índices das colunas de entrada (outras colunas)
    colunas_entrada_indices = list(range(0, 31))  # Índices das colunas de "0" a "31" (A:AF)

    # Índice da coluna alvo (a ser prevista)
    coluna_alvo_indice = 32  # Índice da coluna "32" (AG)

# Criar e treinar o modelo de regressão linear múltipla
model = LinearRegression()
model.fit(df.iloc[:, colunas_entrada_indices], df.iloc[:, coluna_alvo_indice])

# Valores de entrada para previsão
valores_previsao = df.iloc[:, colunas_entrada_indices].tail(1)  # Última linha das colunas de entrada

# Fazer a previsão
y_pred = model.predict(valores_previsao)

# Fazer a previsão
y_pred = model.predict(valores_previsao)

# Calcular o coeficiente de determinação (R²)
y_true = df.iloc[:, coluna_alvo_indice]
r2 = r2_score(y_true, model.predict(df.iloc[:, colunas_entrada_indices]))

# Imprimir o resultado da previsão
print("Valor previsto:", y_pred[0])
print("Coeficiente de Determinação (R²):", r2)

