class Teste:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
