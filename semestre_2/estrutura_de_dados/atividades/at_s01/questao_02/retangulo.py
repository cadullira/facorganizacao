class Retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura
  
  # o método vai testar se os números informandos formam um retângulo
  def eRetangulo(self):
     if (self.largura != self.altura) and (self.largura > 0) and (self.altura > 0):
       return True     
     
  # o método vai calcular o perímetro
  # usando o underline para deixar o método privado a classe
  def calcularPerimetro(self):
    # Perimetro = 2*(largura + altura)
    valido = self.eRetangulo()
    if valido:   
      return f'{2*(self.largura + self.altura)}'
    else:
      return f'Os valores {self.altura} x {self.largura} -> não formam um retângulo, perímetro inválido.'   
  
  # mesma forma usada no método _carlculaPerimetro(self)
  def calcularArea(self):
    # Area = largura * altura
    valido = self.eRetangulo()    
    if valido:
      return f'{self.largura * self.altura}'
    else:
      return f'Os valores {self.altura} x {self.largura} -> não formam um retângulo, área inválida.'   
    
  