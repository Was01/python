import numpy as np

import pandas as pd

from random import choice

##Criando e removendo colunas do dataframe

# Criando colunas

df=pd.read_excel("peso_altura.xlsx")

idade=np.random.randint(19,40,5)

df['Idade']=idade

sexo=[choice(['Masculino','Feminino'])for i in range(5)]

df['Sexo']=sexo

#Renovendo linhas e colunas

df.drop('Altura (cm)',axis=1)

df.drop(0)