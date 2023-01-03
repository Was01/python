import numpy as np
import pandas as pd

dados=np.arange(1,10).reshape(3,3)


df1=pd.DataFrame(dados,columns='A B C'.split())
df2=pd.DataFrame(dados,columns='A B C'.split())
df3=pd.DataFrame(dados,columns='D E F'.split())

## Concatenar

pd.concat([df1,df2],ignore_index=True) ## concatena os datframes na vertical



pd.concat([df1,df3],axis=1)

pd.concat([df1,df2,df3],ignore_index=True)

# Merge

df1=pd.DataFrame(dados,columns='A B C'.split())
df2=pd.DataFrame(dados,columns='D B C'.split())

pd.merge(df1,df2,on=['B','C'])


#Join

df2=pd.DataFrame(dados,columns='D E F'.split() , index=[1,2,3])

df1.join(df2,how='outer')