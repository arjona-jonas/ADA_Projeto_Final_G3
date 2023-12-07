#bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#lendo o arquivo
df = pd.read_csv('../../data/data_raw.csv')

#checando por nulos
print(df.info())

#algumas entradas
print(df.head())

#checando medidas descritivas
print(df.describe())

#checando valores negativos
valores_negativos = df[(df.select_dtypes(include=['int', 'float']) < 0).any(axis=1)].value_counts()
print(f"Quantidade de valores negativos: {valores_negativos.count()}")
print(f"Proporção negativos/total: {(valores_negativos.count()/len(df))*100:.2f}%")

#removendo negativos
ind_negativos = df[(df.select_dtypes(include=['int', 'float']) < 0).any(axis=1)].index
df.drop(ind_negativos,inplace=True)

#checando menores de idade
menores = df['Age']<18
print(f"Usuários menores de idade: {menores.sum()}")
print(f"Proporção de menores sobre o total de usuários: {(menores.sum()/len(df))*100:.2f}%")

#filtrando para maiores de 18 apenas
df.query('Age>=18',inplace=True)

#situacao da base (linhas e colunas)
print(df.shape)

#exportando csv tratado
df.to_csv('../../data/01-intro.csv')