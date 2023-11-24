class Pagina07:
    def exercício01():
        """Números repetidos"""

        list_a = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]
        repeated = set()
        already_seen = set()

        for num in list_a:
            if num in already_seen:
                repeated.add(num)

            if num not in already_seen:
                already_seen.add(num)

        print("Resposta:")
        print(repeated)

    def exercício02():
        """Dados da sorte"""

        rolls = [5, 2, 1, 3, 2, 6, 1, 4, 2, 6, 3, 1]

        already_roll = set()
        sum_seven = []

        for roll in rolls:
            if (7 - roll) in already_roll:
                sum_seven.append((7 - roll, roll))
                already_roll.remove((7 - roll))
            else:
                already_roll.add(roll)

        print("Resposta:")
        print(sum_seven)
        print(already_roll)


Pagina07.exercício02()
