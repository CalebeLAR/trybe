# Para fixar
def identificar(self):
    print(f"Meu carro é um {self.modelo}, da marca.", end=" ")
    print(f"Ele é do {self.ano} e tem a cor {self.cor}.")


class Carro:
    identificar = identificar
    pass


carro01 = Carro()
carro01.modelo = 'conversivel'
carro01.ano = 2023
carro01.cor = 'rosa-choque'

carro01.identificar()
