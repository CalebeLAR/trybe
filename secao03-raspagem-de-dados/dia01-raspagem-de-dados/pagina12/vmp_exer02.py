import requests
import json
# Exercício 2:

# Faça uma requisição ao recurso usuários da API do Github
# (https://api.github.com/users), exibindo o username e url de todos os
# usuários retornados.

response = requests.get('https://api.github.com/users')
users_data = json.loads(response.text)
for user in users_data:
    print(f"user: {user['login']}")
    print(f"url: {user['url']}\n")
