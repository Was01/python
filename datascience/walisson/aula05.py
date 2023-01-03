import numpy as np

array=np.random.randn(10)
print (array)

mtx=np.random.randn(3,3)
print(mtx)

array.ndim

mtx.ndim

array.shape

mtx.shape

array.dtype ## retorna o tipo de 


array.astype(int)

array.min()

array.max()

print(array)
array.min()
array.argmin() ## retorna a posição onde se encontra o menor elemento do array

array.mean()
np.mean(array)

array.sum()
np.sum(array)


array.var()

array.sort() ## ordena o array

mtx.T

## Máscaras

a=np.array([1,2,3,4])


a[a>=3]

a[a%2==0]