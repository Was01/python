import random
from datetime import datetime
## Exemplo1 

random.randint(1,10)

numeros=[]

for i in range(20):
    numero_aleatorio=random.randint(1,10)
    numeros.append(numero_aleatorio)
    
print(numeros)


## Estrutura da list comprenhesion

numeros_lc=[random.randint(1,10) for i in range(20)]

print(numeros_lc)

##Exemplo2

numeros_pares=[i for i in numeros_lc if i%2==0]

print(numeros_pares)

## Exemplo3

texto='P\6*y()t!!!h@@@@@@@@on#333 L987an@@@@@@@@@@@@@gu************age'

texto_formatado_lista=[letra for letra in texto if letra.isspace()or letra.isalpha()]

''.join(texto_formatado_lista)

datas_string=['01/08/2017','17/08/2000','04/05/1997','31/01/2000','26/10/2000']
datas=[ datetime.strptime(data, '%d/%m/%Y').date() for data in datas_string ]