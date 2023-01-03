import numpy as np

b=np.array([[1,2,3],[4,5,6],[7,8,9]])

## métodos

print(b)            #imprime o array 

print(b.ndim)  # imprime a dimensão do array 

print(b.shape) # retorna o número de linhas e colunas do array

print(len(b))  #retorna o número de linhas do array

## Criação usando função

c=np.arange(0,11,0.5)
print(c)


##Arrays comuns

d=np.linspace(1,10,4)
print(d)

e=np.linspace(1,10,4,endpoint=False)
print(e)

f=np.ones((2,5))
print(f)


g=np.zeros((3,4))
print(g)

h=np.random.rand(5,2)
print(h)


i=np.random.randint(1,10,5)
print(i)

j=np.eye(3)
print(j)


k=np.diag([1,2,3,4])
print(k)