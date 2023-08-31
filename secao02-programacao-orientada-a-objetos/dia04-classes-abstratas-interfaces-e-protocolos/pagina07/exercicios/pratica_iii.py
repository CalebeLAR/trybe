from typing import Protocol, Union
import json


PATH = """dia04-classes-abstratas-interfaces-e-protocolos/pagina07/exercicios/\
pratica_iii_messages.json"""


# Exercício 3 – Protocolos

# Implemente uma classe de protocolo para um sistema de mensagens que defina
# os métodos necessários para enviar e receber mensagens. Em seguida, faça
# classes para dois sistemas de mensagens diferentes que implementam o
# protocolo.

# Passos
# Defina uma classe de protocolo chamada MessagingProtocol que defina os
# seguintes métodos:

#     send_message(to: str, message: str) -> bool: envia uma mensagem para o
#     destinatário especificado. Retorna True se a mensagem for enviada com
#     sucesso e False caso contrário.

#     receive_message() -> Union[str, None]: recebe uma mensagem, se houver
#     disponível. Retorna a mensagem como uma string ou None se nenhuma
#     mensagem estiver disponível.

#     Implemente uma classe chamada InMemoryMessaging que implemente o
#     protocolo MessagingProtocol. Nessa classe deve ser usada uma estrutura de
#     dados na memória (por exemplo, um dicionário) para armazenar mensagens.
#     Você pode usar a classe queue.Queue para implementar uma fila de
#     mensagens simples.

#     Implemente uma classe chamada FileMessaging que implemente o protocolo
#     MessagingProtocol. Essa classe deve usar uma abordagem baseada em arquivo
#     para armazenar mensagens. Você pode usar a função interna open() para
#     criar e manipular arquivos.

#     Teste as classes InMemoryMessaging e FileMessaging criando instâncias de
#     cada classe e usando os métodos send_message() e receive_message().

#     Lembre-se de usar o mypy para verificar se a tipagem está correta.


class MessagingProtocol(Protocol):
    def send_message(to: str, message: str) -> bool:
        pass

    def receive_message() -> Union[str, None]:
        pass


class InMemoryMessaging(MessagingProtocol):
    def __init__(self) -> None:
        self.memory = []

    def send_message(self, to: str, message: str) -> bool:
        if not isinstance(message, str):
            return False

        if not self.memory:
            self.memory = [{"to": to, "message": message}]
            return True
        else:
            self.memory.append({"to": to, "message": message})
            return True

    def receive_message(self) -> Union[str, None]:
        if self.memory:
            return self.memory[-1]

        else:
            print("não ná mensagens")
            return None


# inmemory = InMemoryMessaging()
# inmemory.send_message('funalo', 'olá funlano')
# inmemory.send_message('outro fulano', 'olá outro funlano')
# inmemory.send_message('outro fulano', 'olá outro funlano')
# inmemory.send_message('outro fulano', 'olá outro funlano')
# print(inmemory.memory)
# print(inmemory.receive_message())


class FileMessaging(MessagingProtocol):
    def send_message(self, to: str, message: str) -> bool:
        with open(PATH, "r+") as file:
            messages: list = json.load(file)

            if not isinstance(messages, list):
                return False

            messages.append({"to": to, "message": message})
            new = json.dumps(messages)
            file.seek(0)  # Posicionar o cursor no início do arquivo
            file.write(new)  # Escrever os dados atualizados
            file.truncate()  # Truncar qualquer conteúdo restante

    def receive_message(self) -> Union[str, None]:
        with open(PATH, "r") as file:
            messages: list = json.load(file)

            if not messages:
                print("não ná mensagens")
                return None
            else:
                return messages[-1]


fileMessaging = FileMessaging()
fileMessaging.send_message("maria", "ola maria")
print(fileMessaging.receive_message())
