from Calculadora import Calculadora
from Comodo import Comodo

calc = Calculadora()
comodo = Comodo(
            input("Qual a largura do cômodo? "),
            input("Qual a profundidade do cômodo? ")
        )

area_parede = calc.calcular_area_parede(comodo)
area_teto = calc.calcular_area_teto(comodo)

print(" A area da parede é : ", area_parede)
print( "A area do teto é : ", area_teto)
print("A quantidade de litros de tinta necessários é : ", calc.calcular_litragem_necessaria())