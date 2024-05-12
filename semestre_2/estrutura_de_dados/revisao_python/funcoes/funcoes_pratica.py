# soma os elementos de uma lista usando uma função

inteiros = []

def soma_elementos_lista(inteiros):
  soma = 0
  for i in inteiros:
    soma += i
  return soma

somatorio = soma_elementos_lista([10, 20, 2, 1, 5, -32])
print(f'A soma dos números {inteiros} = {somatorio}')