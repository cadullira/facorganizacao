# Um professor de Matemática deseja construir um programa para gerar uma Progressão Aritmética (PA). Para isso, devem ser informados 3 parâmetros de entrada: a) primeiro termo da PA, b) quantidade de termos da PA e c) razão dessa PA. Construa um programa para carregar e imprimir uma lista contendo os termos da PA, bem como a soma dos elementos da PA.

print('Bora construir a PA Professor!')
primeiro_termo = int(input('Me informe o 1° termo da PA.: '))
quantidade_termo = int(input('Me informe também a quantidade de termos.: '))
razao_pa = int(input('Por fim, preciso da razão da PA.: '))

termos = []

i = primeiro_termo

for i in range(1,quantidade_termo + 1):
  termo_pa = primeiro_termo + (i - 1) * razao_pa
  termos.append(termo_pa)
print(termos)

