import pandas as pd
import matplotlib

microdadosEnem=pd.read_csv('MICRODADOS_ENEM_2021.csv',sep=';',encoding='ISO-8859-1')


colunasSelecionadas=['TP_SEXO','NU_NOTA_REDACAO']

microdadosEnemSelecionado=microdadosEnem.filter(items=colunasSelecionadas)


microdadosEnemSelecionado.isna().sum()


microdadosEnemSelecionado=microdadosEnemSelecionado.dropna()


microdadosEnemSelecionado.groupby('TP_SEXO').count()