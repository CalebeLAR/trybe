import requests
from parsel import Selector

# 🚀 Exercício 4:

# Baseando-se em uma página contendo detalhes sobre um livro
# (http://books.toscrape.com/catalogue/the-grand-design_405/index.html), faça
# a extração dos campos título, preço, descrição e url contendo a imagem de
# capa do livro.

# O preço deve vir somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76. A
# descrição deve ter o sufixo “more…” removido quando existir. Os campos
# extraídos devem ser apresentados separados por vírgula. Ex: título, preço,
# descrição, capa.

# Exemplo:

# The Grand Design,13.76,THE FIRST MAJOR WORK... ...be91.jpg

response = requests.get(
    "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
)
selector = Selector(text=response.text)


def get_title():
    return selector.css(
        "article.product_page div.row div.col-sm-6.product_main h1::text"
    ).get()


def get_price():
    return selector.css(
        "article div.row div.col-sm-6.product_main p.price_color::text"
    ).re_first(r"\d+\.\d{2}")


def get_description():
    return (
        selector.xpath("//*[@id='content_inner']/article/p/text()")
        .get()
        .removesuffix(" ...more")
    )


def get_image():
    return (
        selector.css("#product_gallery div div div img::attr(src)")
        .get()
        .replace("../../", "http://books.toscrape.com/")
    )


if __name__ == "__main__":
    description = get_description()
    price = get_price()
    title = get_title()
    image = get_image()
    print(description)
    print(f"{title}, {price}, {image}")
