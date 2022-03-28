from typing import Union


class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Union[Node, None] = None


class LinkedList:
    def __init__(self, value) -> None:
        node = Node(value=value)
        self.head: Union[Node, None] = node
        self.tail: Union[Node, None] = node
        self.length = 1

    def append(self, value) -> None:
        node = Node(value=value)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def prepend(self, value) -> None:
        node = Node(value=value)
        if self.length:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def pop(self) -> None:
        if not self.length:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif self.length > 1 and self.head and self.tail:
            current_node = self.head.next
            penultimate_node = self.head
            while current_node:
                if current_node.next == self.tail:
                    penultimate_node = current_node
                    break
                current_node = current_node.next

            self.tail = penultimate_node
            penultimate_node.next = None
            self.length -= 1

    def pop_first(self) -> None:
        if self.head and self.tail and self.length:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1

    def get(self, index) -> Union[Node, None]:
        if index >= 0 and index < self.length:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next

            return current_node
        return None

    def set_value(self, index, value) -> None:
        if index >= 0 and index < self.length:
            node = self.get(index)
            node.value = value

    def insert(self, index, value) -> None:
        if index == 0 and self.length == 0:
            node = Node(value)
            self.head = node
            self.head = node
        elif index >= 0 and index < self.length:
            if index == 0:
                self.prepend(value=value)
            else:
                new_node = Node(value=value)
                current_node = self.head.next
                previous_node = self.head
                for _ in range(1, index):
                    previous_node = current_node
                    current_node = current_node.next
                previous_node.next = new_node
                new_node.next = current_node

    def remove(self, index) -> None:
        if index >= 0 and index < self.length:
            if index == 0:
                self.head = self.head.next
                if self.length == 1:
                    self.tail = None
                self.length -= 1
            elif index == self.length - 1:
                self.pop()
            else:
                previous_node = self.head
                current_node = self.head.next
                for _ in range(1, index):
                    previous_node = current_node
                    current_node = current_node.next
                previous_node.next = current_node.next
                self.length -= 1

    def reverse(self):
        next_node = self.head.next
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def __str__(self) -> str:
        output = ""
        current_node = self.head
        while current_node:
            output = output + f"{current_node.value}->"
            current_node = current_node.next
        return output + "null"


if __name__ == "__main__":
    llist = LinkedList(4)
    llist.prepend(3)
    llist.prepend(2)
    llist.prepend(7)
    llist.append(10)
    llist.append(14)
    print(llist)
    llist.reverse()
    print(llist)
    llist1 = LinkedList(6)
    print(llist1)
    llist1.reverse()
    print(llist1)
    print(llist.get(2).value)
    print(llist.get(5).value)
    llist.set_value(2, 8)
    llist.set_value(5, 16)
    print(llist.get(2).value)
    print(llist.get(5).value)
    print(llist)
    llist.pop()
    print(llist)
    llist.pop()
    print(llist)
    llist.remove(3)
    print(llist)
    llist.remove(2)
    print(llist)
    llist.insert(1, 12)
    print(llist)
    llist.insert(2, 10)
    print(llist)
