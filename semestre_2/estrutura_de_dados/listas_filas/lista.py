import random
# # declara uma lista

# atrizes = []
# atores = ['Caio Blat', 'Fábio Assunção', 'Vladimir Bricchia']

# # for ator in atores:
# #   print(ator)

# # adiciona elemento
# # append, insert
# # append adiciona elemento final da lista
# # insert adiciona elemento passando também a posição, atrizes('nomeDaAtriz', 0)

# atrizes.append('Paolla Oliveira')
# atores.insert(1,'João Grilo')

# # embralha e escolhe algum elemento
# # shuffle de random -> embaralha
# # choice -> realiza uma escolha de elemento da lista

# numeros = [10, 2, 3, 5, -50, 4, 1]

# random.shuffle(numeros)
# sorteado = random.choice(numeros)

# #print(sorteado)

# # ordena elemntos

# numeros.sort(reverse=True)

# # for numero in numeros:
# #   print(numero)

# # remover elemento de uma lista
# # remove, pop, del

# #numeros.remove(7) # se o elemento passado como parâmetro não estiver na lista vai dá erro
# print(numeros)

# #numeros.pop() # passa a posição do elemento que desejo excluir, se não passar nada, será removido da lista o último elemento

# #del numeros[3]

# #esvaziar lista

# #numeros.clear() # limpa lista

# # fazer copia de uma lista

# copia = list(atores)

# print(copia)

# if copia == atores:
#   atores.clear()
#   print('Lista esvaziada!')
# else:
#   print('Erro, copia gerada não igual a original')

# atores_gringos = ['Brad Pitt', 'Leonardo di Capri', 'Antônio Bandeiras']


# # método extend adiciona uma lista dentro de outra
# copia.extend(atores_gringos)

# print(copia)

# numeros.append(10)
# numeros.append(10)
# numeros.append(10)
# numeros.append(1)
# numeros.append(2)

# print(numeros)

# # método count vai contar quantas vezes certo valor informado aparece na lista
# conta_elemento = numeros.count(10)

# print(conta_elemento)

# # método len vai informar quantos elementos contém na lista
# print(len(numeros))

# # métodos max(), min(), sum()

# maior = max(numeros) # maior número
# menor = min(numeros) # menor número
# soma = sum(numeros) # somatório dos números
# media = soma / len(numeros)

# print(f'Maior => {maior}, Menor => {menor}, Soma => {soma}, Média => {media}')

# indice = copia.index('João Grilo')
# print(indice)

# #ator = input('Informe o nome do ator: ')
# ator = 'Brad Pitt'
# verifica = ator

# if verifica in copia:
#   indice = copia.index(verifica)
#   print(f'{verifica} está no índice {indice}.')
# else:
#   print(f'{verifica} não está na lista.')

# # enumerate método para obtermos não só a informação mais também o índice
# for indice, nome in enumerate(copia):
#   print(f'{nome} está armazenado no índice {indice}')

# # matriz

# lista_numeros = [[10, 10, 3], [1, 4, 10], [1, 2, 5]]

# # lista_numeros[0][0] = 0
# # lista_numeros[0][1] = 2
# # lista_numeros[0][2] = 1

# # print(f'lista de números = {lista_numeros[0][0]}, {lista_numeros[0][1]}, {lista_numeros[0][2]}')

# print(lista_numeros)
# lista_numeros = []

# #for i in range(len(lista_numeros) - 1):
#   #for j in range

# while True:
#   linha = int(input('Informe a quantidade de linhas: '))
#   coluna = int(input('Informe a quantidade de colunas: '))

#   if linha > 0 and coluna > 0:
#     for i in range(linha):
#       l = []
#       for j in range(coluna):
#         num = random.randint(1, 101)
#         l.append(num)
#       lista_numeros.append(l)
#     break
# #print(lista_numeros)

# for i in range(linha):
#   for j in range(coluna):
#     print(lista_numeros[i][j], end=" ")
#   print("")
matriz = []
ordem = int(input('Informe a ordem da matriz: '))
if ordem >= 2:
  while True:
 
    for i in range(ordem):
      l = []
      for j in range(ordem):
        num = int(input(f'Informe o {j+1}º elemento da {i+1}ª linha: '))
        l.append(num)
      matriz.append(l)
    break

  DP = []
  DS = []

  for i in range(ordem):
    for j in range(ordem):
      print(matriz[i][j], end=" ")
      if i == j:
        DP.append(matriz[i][j])
      if i + j == (ordem - 1):
        DS.append(matriz[i][j])
    print("")

  maiorDP = max(DP)
  menorDS = min(DS)

  media = (maiorDP + menorDS) / 2
  print(f'Diagonal principal.: {DP}')
  print(f'Diagonal secundária.: {DS}')
  print(f'Média.: {round(media, 2)}')
else:
  print('Informe uma ordem válida.')















