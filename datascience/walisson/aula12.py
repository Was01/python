import pandas as pd
import numpy as np

dados =np.array([[1,2,np.nan],[4,np.nan,np.nan],[7,8,9]])
df=pd.DataFrame(dados,columns='A B C'.split())

df.isnull()

df['C'].isnull().sum()


df.dropna() ## exclui todas as linhas que possuem dados ausentes

df.dropna(axis=1) ## exclui todas as colunas que possuem dados ausentes

df['B'].fillna(0) ## prenche campo ausente com valor específico

df.fillna(method='ffill')

df.fillna(method='bfill')


df=pd.read_csv('titanic_train.csv')

df.head()

df.isnull().sum()

df.shape

df.drop('Cabin',axis=1,inplace=True)

df.isnull().sum()

df['Embarked'].value_counts()


df['Embarked'].fillna('S',inplace=True)

df.isna().sum()

df['Age'].mean()

df['Age'].fillna(df['Age'].mean(),inplace=True)

df.isnull().sum()