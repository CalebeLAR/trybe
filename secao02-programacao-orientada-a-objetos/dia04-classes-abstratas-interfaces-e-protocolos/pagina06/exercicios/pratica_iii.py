from typing import Protocol, Union, TypedDict

# Exercício 3 – Protocolos

# Implemente uma classe de protocolo para um sistema de mensagens que defina
# os métodos necessários para enviar e receber mensagens. Em seguida, faça
# classes para dois sistemas de mensagens diferentes que implementam o
# protocolo.

# Passos
# Defina uma classe de protocolo chamada MessagingProtocol que defina os
# seguintes métodos:


class MessagingProtocol(Protocol):
    def send_message(to: str, message: str) -> bool:
        pass

    def receive_message() -> Union[str, None]:
        pass


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


class Message(TypedDict):
    to: str
    message: str


class InMemoryMessaging(MessagingProtocol):
    def __init__(self) -> None:
        self.messages = list[Message]
    

    


#     Implemente uma classe chamada FileMessaging que implemente o protocolo
#     MessagingProtocol. Essa classe deve usar uma abordagem baseada em arquivo
#     para armazenar mensagens. Você pode usar a função interna open() para
#     criar e manipular arquivos.

#     Teste as classes InMemoryMessaging e FileMessaging criando instâncias de
#     cada classe e usando os métodos send_message() e receive_message().

#     Lembre-se de usar o mypy para verificar se a tipagem está correta.
