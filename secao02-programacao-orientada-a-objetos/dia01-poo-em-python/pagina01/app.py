def add_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


print(add_two_numbers(1, 0))


# tipo int é inferido sem que eu precise deixar explícito
var1 = 1

# não faça isso, é verboso e desnecessário
var2: int = 1

# importante deixar explícito que começa como int, mas pode mudar para float
var3: int | float = 1
