class ParaFixar01:
    def exercicio01():
        print("""
        1.Qual a importância de debugar o código?
        Resposta:
        garantir o bom funcionamento e entendimento do mesmo

        2.Quais as vantagens de usar debugger do VS Code?
        Resposta:
        eficiencia e faciliedade na visualição das variaveis do codigo

        3.Quais são as formas mais comuns de debugar código em Python?
        Resposta:
        a primeira é por tentativa e erro: Print e executar o codigo
        a segunda é pela ferramenta de depuração: Usando o debugger
        """)

    def exercicio02():
        print("")
        print("Considere o exemplo de código em math.py")
        print("")
        print("Sem alterar o código, descubra qual exceção é levantada se:")
        print("1.Um dos elementos da input_list for um inteiro negativo.")
        print("Resposta:")
        print("Ocorreu uma exceção: ValueError")
        print("ValueError: factorial() not defined for negative values")
        print("")
        print("2.Um dos elementos da input_list for uma string.")
        print("Resposta:")
        print("Ocorreu uma exceção: TypeError")
        print("TypeError: 'str' object cannot be interpreted as an integer")


if __name__ == "__main__":
    ParaFixar01.exercicio01()
    # ParaFixar01.exercicio02()
