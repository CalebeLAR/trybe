import sys

user_input = input("Digite uma mensagem: ")
print('O valor recebido foi:', user_input)


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)
