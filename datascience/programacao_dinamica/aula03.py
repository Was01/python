import pandas as pd

microdadosEnem=pd.read_csv('MICRODADOS_ENEM_2021.csv',sep=';',encoding='ISO-8859-1')

colunasSelecionadas=['TP_FAIXA_ETARIA', 'TP_SEXO',
       'TP_ESTADO_CIVIL', 'TP_COR_RACA', 'TP_NACIONALIDADE',
       'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO',
       'IN_TREINEIRO', 'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC',
       'CO_UF_ESC', 'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC',
       'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC', 'CO_MUNICIPIO_PROVA',
       'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'SG_UF_PROVA',
       'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC',
       'TP_PRESENCA_MT', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC',
       'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC',
       'NU_NOTA_MT', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH',
       'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA',
       'TX_GABARITO_CN', 'TX_GABARITO_CH', 'TX_GABARITO_LC',
       'TX_GABARITO_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_COMP1',
       'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5',
       'NU_NOTA_REDACAO']

microdadosEnemSelecionado=microdadosEnem.filter(items=colunasSelecionadas)

coluna_NO_MUNICIPIO_ESC=microdadosEnemSelecionado['NO_MUNICIPIO_ESC']

coluna_TP_SEXO=microdadosEnemSelecionado['TP_SEXO']

coluna_SG_UF_ESC=microdadosEnemSelecionado['SG_UF_ESC']

coluna_NO_MUNICIPIO_ESC.value_counts().sort_index()

coluna_TP_SEXO.value_counts()

coluna_SG_UF_ESC.value_counts()

coluna_SG_UF_ESC.hist(bins=27)