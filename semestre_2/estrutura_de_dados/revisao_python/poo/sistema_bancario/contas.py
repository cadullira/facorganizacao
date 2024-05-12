class Conta:
  def __init__(self, numero, saldo, cliente):
    self.numero = numero
    self.saldo = saldo
    self.cliente = cliente

  def exibir_saldo(self):
    print(f'Conta: {self.numero} || ', end='')
    print(f'Cliente: {self.cliente.nome}')
    print(f'Saldo: R$ {self.saldo:.2f}. \n')

  def sacar(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      print('Você realizou uma operação de SAQUE')
      print(f'Valor SACADO R$ {valor}.')
    else:
      print('Você tentou realizar uma operação de SAQUE')
      print('Saldo insuficiente!')

  def depositar(self, valor):
    self.saldo += valor
    print('Você realizou uma operação de DEPÓSITO')
    print(f'Valor DEPOSITADO R$ {valor}')
