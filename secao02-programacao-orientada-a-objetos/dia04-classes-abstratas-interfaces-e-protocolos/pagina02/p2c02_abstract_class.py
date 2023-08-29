import abc


class InterfaceFormal(abc.ABC):
    @abc.abstractmethod
    def exemplo(self):
        pass


teste = InterfaceFormal()
# >>> TypeError: Can´t instantiate abstract class InterfaceFormal with
# abstract methods exemplo
