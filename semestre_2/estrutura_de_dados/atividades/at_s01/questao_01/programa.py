# 1. Crie uma classe chamada Ingresso, que possua o nome do evento e o valor do ingresso. Crie o método exibirValor(), que apenas retorne o valor do ingresso. Crie o método __str__ que retorne o nome do evento seguido do valor do ingresso. Crie um programa para testar sua classe.

from ingresso import Ingresso

ingresso1 = Ingresso('Festa Casca de Bala', 50)
ingresso2 = Ingresso('Festa Casca de Bala', 200)

valor_ingresso1 = ingresso1.exibirValor()
valor_ingresso2 = ingresso2.exibirValor()
print(valor_ingresso1)
print(valor_ingresso2)
print(ingresso1)
print(ingresso2)
