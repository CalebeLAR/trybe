class Product:
    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price
        pass

    def __str__(self):
        return str({"id": self.id, "name": self.name, "price": self.price})

    pass
