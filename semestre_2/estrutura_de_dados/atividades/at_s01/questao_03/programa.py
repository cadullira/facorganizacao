from ponto import Ponto 

pontos = []
adiciona = 'S'

while adiciona == 'S':
  nome = input('Informe um nome: ')
  x = int(input('Informe um número: '))
  y = int(input('Informe outro número: '))

  p = Ponto(nome, x, y)
  pontos.append(p)

  opcao = input('Deseja adicionar mais outro ponto? Digite S se sim. ')
  adiciona = opcao.upper()

for ponto in pontos:
  print(ponto)

