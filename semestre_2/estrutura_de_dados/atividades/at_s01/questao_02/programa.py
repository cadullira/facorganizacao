# 2. Crie uma classe chamada Retangulo, a qual possua os atribu tos largura e altura, e os métodos calcularPerimetro() e calcularArea(). No código de teste, crie um objeto e calcule, respectivamente, o perímetro e a área desse retângulo.

from retangulo import Retangulo

altura = float(input('Informe um valor para altura: '))
largura = float(input('Informe um valor para largura: '))

r1 = Retangulo(altura, largura)

perimetro = r1.calcularPerimetro()
area = r1.calcularArea()

print(perimetro)
print(area)


