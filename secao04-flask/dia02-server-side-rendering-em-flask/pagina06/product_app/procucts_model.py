class Product:
    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price
        pass

    def __str__(self):
        return str({"id": self.id, "name": self.name, "price": self.price})

    pass


list_procucts = [
    {"name": "Smartphone", "price": 799.99},
    {"name": "Notebook", "price": 1299.99},
    {"name": "Televisor", "price": 499.99},
    {"name": "Liquidificador", "price": 89.99},
    {"name": "Máquina de Lavar Roupa", "price": 699.99},
    {"name": "Refrigerador", "price": 899.99},
    {"name": "Aspirador de Pó", "price": 129.99},
    {"name": "Forno de Micro-ondas", "price": 149.99},
    {"name": "Secadora de Roupas", "price": 499.99},
    {"name": "Cafeteira Elétrica", "price": 69.99},
]
products = []
for _id, product in enumerate(list_procucts):
    products.append(Product(_id, product["name"], product["price"]))

for product in products:
    print(product)
