## Filtrando dados

import numpy as np
import pandas as pd

df=pd.read_csv('titanic_train.csv')

df.head()

df.columns ## exibe os títulos das colunas

df.index


df['Sex'].unique()

df['Age'].unique()


df['Sex'].value_counts()

df['Age'].value_counts()

df['Age'].mean()


##Filtragem de dados

df[df['Age']>25]

df[df['Sex']=='female']