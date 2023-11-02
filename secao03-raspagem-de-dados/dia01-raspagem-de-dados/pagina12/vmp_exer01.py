import requests

# Exercício 1:

# Faça uma requisição ao site https://httpbin.org/encoding/utf8 e exiba seu
# conteúdo de forma legível.

response = requests.get("https://httpbin.org/encoding/utf8")
print(response.text)

# Exercício 2:

# Faça uma requisição ao recurso usuários da API do Github
# (https://api.github.com/users), exibindo o username e url de todos os
# usuários retornados.

response = requests.get('https://api.github.com/users')
print((response.text))
