import pandas as pd
import numpy as np

df=pd.read_csv('titanic_train.csv',sep=',')

df.head() # Exibe as cinco primeiras linhas do datasheet

df.describe() ##Faz uma desscrição dos dados

dados=pd.read_excel('peso_altura.xlsx',sheet_name='Planilha1')

dados.head()

dados.shape

dados.to_csv('peso_altura.csv')