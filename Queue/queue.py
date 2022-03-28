from typing import Union


class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Union[Node, None] = None


class Queue:
    def __init__(self, value) -> None:
        node = Node(value=value)
        self.first = node
        self.last = node
        self.length = 1

    def enqueue(self, value):
        node = Node(value=value)
        if self.length:
            self.last.next = node
            self.last = node
        else:
            self.first = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.length:
            temp = self.first
            if self.length == 1:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
                temp.next = None
            self.length -= 1
            return temp.value

    def __str__(self) -> str:
        output = ""
        current_node = self.first
        while current_node:
            output = output + f"{current_node.value}->"
            current_node = current_node.next
        return f"{output}null length = {self.length}"


if __name__ == "__main__":
    queue = Queue(4)
    print(queue)
    queue.enqueue(3)
    print(queue)
    queue.enqueue(2)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.enqueue(8)
    print(queue)
