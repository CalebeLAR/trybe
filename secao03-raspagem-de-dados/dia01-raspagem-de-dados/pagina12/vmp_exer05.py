import requests
from parsel import Selector
import vmp_exer04

# 🚀 Exercício 5:
# Modifique o exercício anterior para retornar também quantos livros estão
# disponíveis, apresentando como último campo no retorno.

response = requests.get(
    "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
)
selector = Selector(text=response.text)


def get_availability():
    return (
        selector.xpath(
            "//*[@id='content_inner']/article/table/tr[6]/td/text()"
        )
        .get()
        .replace("In stock (", "")
        .replace(" available)", "")
    )


print(vmp_exer04.get_description())
print(
    f"{vmp_exer04.get_title()}, {vmp_exer04.get_price()}, "
    f"{vmp_exer04.get_image()}, {get_availability()}"
)
