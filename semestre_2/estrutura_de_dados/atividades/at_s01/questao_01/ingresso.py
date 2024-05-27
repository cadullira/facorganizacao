class Ingresso:
  
  def __init__(self, nome_evento, valor_ingresso):
    self.nome_evento = nome_evento
    self.valor_ingresso = valor_ingresso

  def exibirValor(self):
    return self.valor_ingresso
  
  def __str__(self) -> str:
    return f'Evento: {self.nome_evento} - Valor: R$ {self.valor_ingresso}'
