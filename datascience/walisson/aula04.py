import numpy as np

## Operações com arrays numpy

## Com escalares

a1=np.ones(10)
print (a1)


print(a1*10)

a2=np.random.randint(1,20,size=(2,4))

print(a2*10)

##Entre arrays

b1=np.array([[1,2,3],[4,5,6],[7,8,9]])
b2=np.array([[1,0,0],[0,1,0],[0,0,1]])

b=b1.dot(b2) ## Multiplicação de matrizes

print(b)


## Comparações

c1=np.array([1,2,2,1])
c2=np.array([1,2,2,9])

c1==c2 ## compara dos arrays elemento a elemento

np.array_equal(c1,c2) ## compara o conteúdo inteiro de dois arrays