class Ponto:

  def __init__(self, nome, x, y):
    self.nome = nome
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return f'{self.nome}: ({self.x}, {self.y})'