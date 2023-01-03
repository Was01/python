import pandas as pd
import numpy as np

##Series

d={'Python':10,'JavaScript':9,'Matlab':7}
series=pd.Series(d)

##indexação

s=pd.Series(data=np.random.randint(1,5,10),index='A B C D E F G H I J'.split())
print(s)


##Operações

s1=pd.Series(data=np.random.randint(1,100,3),index='Facebook Instagram Youtube'.split())
s2=pd.Series(data=np.random.randint(1,100,3),index='Facebook Instagram Youtube'.split())

s1+s2

##Máscaras

s[s>2]