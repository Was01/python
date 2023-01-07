import pandas as pd
import matplotlib



microdadosEnem=pd.read_csv('MICRODADOS_ENEM_2021.csv',sep=';',encoding='ISO-8859-1')

colunasSelecionadas=['TP_SEXO','NU_NOTA_REDACAO']

microdadosEnemSelecionado=microdadosEnem.filter(items=colunasSelecionadas)

microdadosEnemSelecionado=microdadosEnemSelecionado.dropna()


microdadosEnemSelecionado.groupby('TP_SEXO').count()

microdadosEnemSelecionado.groupby('TP_SEXO').max()

microdadosEnemSelecionado.groupby('TP_SEXO').min()

microdadosEnemSelecionado[microdadosEnemSelecionado['NU_NOTA_REDACAO']>0].groupby('TP_SEXO').min()

microdadosEnemSelecionado.groupby('TP_SEXO').mean()


microdadosEnemSelecionado.groupby('TP_SEXO').median()


microdadosEnemSelecionado.groupby('TP_SEXO').hist(bins=30)


microdadosEnemSelecionado.groupby('TP_SEXO').describe()