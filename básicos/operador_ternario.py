
## Exemplo1

numero=int(input('Informe um número inteiro positivo: '))

resultado='par' if numero%2==0 else 'ímpar'

print(f"\nO número {numero} é {resultado}.")


##Exemplo 2

from random import randrange

movimentacoes=[randrange(-1000,1000)for i in range(10)]

print(movimentacoes)


operacoes=['saque' if mov<0 else 'depósito' for mov in movimentacoes]
print(operacoes)