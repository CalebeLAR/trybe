# Exercício 6

# Com base no exercício anterior, instancie um objeto da classe Retangulo com
# os valores base = 5 e altura = 10 e chame os métodos calcular_area e
# calcular_perimetro. Observe como quem usa a classe não precisa entender como
# o calculo é feito.

from para_fixar05 import Retangulo


if __name__ == "__main__":
    retangulo = Retangulo(5, 10)
    print(retangulo.calc_area())
    print(retangulo.calc_perimetro())
