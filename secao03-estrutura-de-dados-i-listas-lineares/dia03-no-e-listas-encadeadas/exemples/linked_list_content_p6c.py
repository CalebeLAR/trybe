from node_p06c import Node


class LinkedList:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __str__(self):
        return f"LinkedList(len={self.__length}, value={self.head_value})"

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def insert_last(self, value):
        last_value = Node(value)
        current_value = self.head_value

        while current_value.next:
            current_value = current_value.next
        current_value.next = last_value
        self.__length += 1


if __name__ == "__main__":

    linkedList1 = LinkedList()
    print(linkedList1)
    linkedList1.insert_first('01:head')
    print(linkedList1)
