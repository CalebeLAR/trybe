# Instanciando a classe Dict
employee_registry = dict()

# Inserindo dados
# objeto[chave] = valor
employee_registry[14] = "name1"
employee_registry[23] = "name2"
employee_registry[10] = "name3"
employee_registry[9] = "name4"
print(employee_registry)

# Alterando o nome do id 10
# objeto[chave] = novo_valor
employee_registry[10] = "name30"
print(f"Novo valor do id 10, após a atualização: {employee_registry[10]}")

# imutaveis
# - int;
# - float;
# - string;
# - tuple;
# - range;
# - byte;
# - frozenset

# Instanciação do objeto vazio
dict1 = {}
dict2 = dict()

# Instanciação com preenchimento inicial de dados
dict3 = {1: "name1", 2: "name2"}
print(f"Dicionário 1: {dict1}")
print(f"Dicionário 2: {dict2}")
print(f"Dicionário 3: {dict3}")

# Inserção e Alteração
# Se a chave não existir no dict, uma nova entrada será criada
# Se já existir, o valor será sobreposto
dict1[14] = "name1"
print(f"Novo dicionário 1, pós inserção/alteração: {dict1}")

# Consulta e Remoção
# Se a chave não existir no dict, causa erro
name = dict1[14]
del dict1[14]
print(f"Dicionário 1 pós consulta e deleção: {dict1}")


# Consulte a forma de se criar um dicionário chamado de dict comprehension e
# crie um dicionário que mapeia inteiros de 3 a 20 para o seu dobro.

exer05 = {}
double = {i: i * 2 for i in range(3, 21)}

for k in range(3, 21):
    exer05[k] = k * 2


# Exemplo:
string = "bbbbaaaacccaaaaaaddddddddccccccc"
# saída: {'b': 4, 'a': 10, 'c': 10, 'd': 8}
exer06 = {}

for letter in string:
    try:
        exer06[letter] += 1
    except Exception:
        exer06[letter] = 1

count_chars = {}

for char in string:
    if char not in count_chars:
        count_chars[char] = 1
    else:
        count_chars[char] += 1

print(count_chars)


exer07 = {}

for k in range(3, 21):
    if k % 2 == 0:
        exer07[k] = k * 2
    else:
        exer07[k] = k * 3

for key in double.keys():
    if key % 2 != 0:
        double[key] = key * 3

print("<=================================>")
print(exer07)
