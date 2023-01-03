import pandas as pd
import numpy as np

##  Agrupando dados de um dataframe


df=pd.read_csv("titanic_train.csv")

df_survived=df.groupby('Survived')

df_survived.mean()

df_sex=df.groupby('Sex').mean()