from typing import Union


class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Union[Node, None] = None
        self.prev: Union[Node, None] = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        node = Node(value)
        self.head: Union[Node, None] = node
        self.tail: Union[Node, None] = node
        self.length = 1

    def append(self, value) -> None:
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop(self) -> None:
        temp = self.tail
        self.tail = self.tail.prev
        temp.prev = None
        self.tail.next = None
        self.length -= 1

    def prepend(self, value) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop_first(self) -> None:
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
        self.length -= 1

    def get(self, index) -> Union[Node, None]:
        node = self.head
        for _ in range(1, index):
            node = node.next
        return node

    def set_value(self, index, value) -> None:
        node = self.get(index)
        node.value = value

    def insert(self, index, value) -> None:
        node = Node(value)
        node_at_index = self.get(index)
        node_before_index = node_at_index.prev
        node_before_index.next = node
        node.prev = node_before_index
        node_at_index.prev = node
        node.next = node_at_index
        self.length += 1

    def remove(self, index) -> None:
        node_at_index = self.geet(index)
        node_before_index = node_at_index.prev
        node_after_index = node_at_index.next
        node_at_index.next = None
        node_at_index.prev = None
        node_before_index.next = node_after_index
        node_after_index.prev = node_before_index
        self.length -= 1
