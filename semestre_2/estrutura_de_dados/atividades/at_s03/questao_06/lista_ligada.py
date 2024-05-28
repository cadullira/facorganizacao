# importar a biblioteca numpy, e faz uma aliase para no
#import numpy as np

# Define a class com o nome No
class No:

    # método construtor, recebe como parâmetro o self faz referência a própria classe, e valor, que é passado quando instaciamos um objeto nó
    def __init__(self, valor):
        self.valor = valor
        # como ainda não existe próximo, atribuimos None para a variável
        self.proximo = None

    # método para mostrar nó, onde é dado simplemeste um print em valor
    def mostrar_no(self):
        print(self.valor)

# Define a class com o nome Lista_Encadeada, responsável pela manipulação da estrutura de uma Lista
class Lista_Encadeada:

    # método construtor da class Lista_Encadeada, não recebe nada como entrada
    # no construtor vai possuir uma referência para o primeiro elemento da lista que inicialmente se encontra vazio
    def __init__(self):
       self.primeiro_lista = None 

    # método de inserção de elemento na lista, recebe como parâmetro self, e o valor a ser inserido na lista
    def inserir_inicio(self, valor):

        # novo recebe algo a ser adicionado, no caso, da class No o objeto instanciado 
        novo = No(valor)

        # a variável novo_proximo vai funcionar como variável auxiliar, que receberá o valor de primeiro_lista no caso None
        novo_proximo = self.primeiro_lista

        # primeiro_lista recebe novo, que contém o objeto advindo da class nó
        self.primeiro_lista = novo