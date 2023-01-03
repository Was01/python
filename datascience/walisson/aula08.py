import pandas as pd
import numpy as np

## Criando um dataframe

dados=np.array([[72,180,26],[80,170,19],[60,165,15]])


df=pd.DataFrame(dados,columns=['Peso','Altura','Idade'],index=['A','B','C'])

##Acessando as colunas


print(df['Altura'])

##Acessando as linhas

print(df.loc['A'])

##Acessando elemento específico
print(df['Peso']['A'])

print(df.loc['C']['Altura'])

##Acessando mais de uma coluna

print(df[['Altura','Idade']])


print(df.iloc[2][0])