from typing import Union


class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Union[Node, None] = None


class Stack:
    def __init__(self, value) -> None:
        node = Node(value=value)
        self.top = node
        self.length = 1

    def push(self, value):
        node = Node(value=value)
        if self.top:
            node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None
            self.length -= 1
            return node.value

    def __str__(self) -> str:
        output = ""
        current_node = self.top
        while current_node:
            output = output + f"{current_node.value}->"
            current_node = current_node.next
        return f"{output}null length = {self.length}"


if __name__ == "__main__":
    stack = Stack(value=4)
    print(stack)
    stack.push(3)
    stack.push(6)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)
    empty_stack = Stack(3)
    print(empty_stack)
    empty_stack.pop()
    print(empty_stack)
    empty_stack.pop()
    print(empty_stack)
    empty_stack.push(8)
    print(empty_stack)
