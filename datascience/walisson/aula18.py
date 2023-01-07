import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




df=pd.read_csv("life_expectancy.csv")

df['Country'].unique()

df.drop('Unnamed: 0',axis=1,inplace=True)

df_brazil=df[df['Country']=='Brazil']

df_eua=df[df['Country']=='EUA']


##Subplots

figure,axes=plt.subplots(nrows=1,ncols=2,figsize=(14,5))
axes[0].plot(df_brazil['Year'],df_brazil['Life Expectancy'],marker='o')
axes[0].set_xlabel('Ano')
axes[0].set_ylabel('Expectativa de Vida')
axes[0].set_title('Dados do Brazil')
axes[1].plot(df_eua['Year'],df_eua['Life Expectancy'],marker='o')
axes[1].set_xlabel('Ano')
axes[1].set_ylabel('Expectativa de Vida')
axes[1].set_title('Dados dos EUA')