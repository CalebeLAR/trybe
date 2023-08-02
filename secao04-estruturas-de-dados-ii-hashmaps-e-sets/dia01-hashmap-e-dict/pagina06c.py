lista = [
    1,
    2,
    3,
    4,
    4,
    6,
    6,
    5,
    5,
    5,
    5,
    8,
    8,
]

memoria = {}
mais_se_repete = 0

for num in lista:
    if num not in memoria:
        memoria[num] = 1
    else:
        memoria[num] += 1

    if memoria[num] >= mais_se_repete:
        mais_se_repete = num

print(mais_se_repete)

