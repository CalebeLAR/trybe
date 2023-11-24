class ParaFixarI:
    def exercício01():
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

    def exercício02():
        words = [
            "pra",
            "amassa",
            "Brasa",
            "do",
            "Santo",
            "vestido",
            "Vem",
            "Braga",
            "quem",
            "Jogar",
            "ama",
            "no",
            "joana",
            "quente",
        ]

        initials_and_words = {}
        for word in words:
            initial_letter = word[0].lower()

            if initial_letter in initials_and_words:
                words = initials_and_words[initial_letter]
                initials_and_words[initial_letter].append(word)

            if initial_letter not in initials_and_words:
                initials_and_words[initial_letter] = [word]

        print("Resposta:")
        for initial, word in initials_and_words.items():
            print(f"{initial}: {word}")

    def exercício03():
        listA = [1, 2, 3, 3, 4, 5]
        listB = [3, 3, 4, 5, 6, 7]
        intersection = {}

        dictA = {}
        dictB = {}
        for index in range(len(listA)):
            a = listA[index]
            b = listB[index]
            if a not in dictA:
                dictA[a] = a

            if b not in dictB:
                dictB[b] = b

            if a in dictB:
                intersection[a] = a

        print(intersection.keys())


ParaFixarI.exercício03()
