import requests

# Exercício 3:

# Às vezes, você precisa fazer com que o seu raspador da Web pareça estar
# fazendo solicitações HTTP como o navegador, para que o servidor retorne os
# mesmos dados que você vê no seu navegador. Faça uma requisição a
# https://scrapethissite.com/pages/advanced/?gotcha=headers e verifique se foi
# bem sucedida.

headers = {
    # "Host": "www.scrapethissite.com",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 109.0) Gecko/"
    "20100101 Firefox/117.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
    "avif,image/webp,*/*;q=0.8",
    # "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Connection": "keep-alive",
    # "Cookie": "_gcl_au=1.1.1665601247.1694100291... ...d1eb93313477",
    # "Upgrade-Insecure-Requests": "1",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "none",
    # "Sec-Fetch-User":  "?1",
    # "TE": "trailers",
}

response = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers",
    headers=headers,
)

print(response.status_code)

assert (
    "User-Agent value doesn't look like a standard mozilla/chrome/safari value"
    not in response.text
)

# Para verificar se a requisição foi bem sucedida, faça (assert
# "User-Agent value doesn't look like a standard mozilla/chrome/safari value"
# not in response.text). Se nada acontecer, seu código está funcionando.
# Faça a inspeção de como a requisição é feita pelo navegador para conseguir
# replicar através do código.
