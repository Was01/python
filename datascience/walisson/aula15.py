import numpy as np

import pandas as pd

df=pd.read_csv('titanic_train.csv')

df['Age'].apply(np.sqrt)


## Método apply

def changeSurvived(elemento):
    if elemento==0:
        return 'No'
    else:
        return 'Yes'
    
df['Survived'].apply(changeSurvived)

df['Fare'].dtype


def changeFare(elemento):
    return '${:.2f}'.format(elemento)

df['Fare'].apply(changeFare)

##Ordenação

df_sort=df.sort_values(by='Age')

df_sort.dropna()