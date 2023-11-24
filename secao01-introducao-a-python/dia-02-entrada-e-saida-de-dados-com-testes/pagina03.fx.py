def exercicio01():
    """
    exercicio01: Faça um programa que solicite o nome de uma pessoa usuária
    e imprima-o na vertical.
    """
    inputName = input("digite seu nome: ")
    for letter in inputName:
        print(letter)


def exercicio02():
    """
    Escreva um programa que receba vários números naturais e calcule a soma
    desses valores. Caso algum valor da entrada seja inválido
    (por exemplo uma letra), uma mensagem deve ser exibida na saída de erros
    no seguinte formato: “Erro ao somar valores, {valor} é um valor inválido”.
    Ao final, você deve imprimir a soma dos valores válidos.
    """
    print(exercicio02.__doc__)

    # input("digite varios numeros separando-os por espaço: ")
    inputNumbers = '1 2    3  4'

    letters = inputNumbers.split(" ")
    sum = 0
    lastLatter = ''

    try:
        for letter in letters:
            lastLatter = letter
            sum += int(letter)
        print(sum)
    except Exception as e:
        print(e)
        print(f'"{lastLatter}" não é do timpo int')


ParaFixar01 = {
    "Exercício01": exercicio01,
    "Exercício02": exercicio02,
}

ParaFixar01["Exercício02"]()
