from typing import Union


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        node = Node(value=value)
        if not self.root:
            self.root = node
        else:
            parent = self.root
            while parent:
                if value > parent.value:
                    if parent.right is None:
                        parent.right = node
                        return
                    parent = parent.right
                elif value < parent.value:
                    if parent.left is None:
                        parent.left = node
                        return
                    parent = parent.left
                else:
                    return None

    def find(self, value) -> Union[Node, None]:
        node = self.root
        while node:
            if value > node.value:
                node = node.right
            elif value < node.value:
                node = node.left
            else:
                return node

    @staticmethod
    def min_value_node(current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    @staticmethod
    def max_value_node(current_node):
        while current_node.right:
            current_node = current_node.right
        return current_node

    # TODO Implement remove method
    # def remove(self, value):
    #     if self.root:
    #         pass
    # parent = self.root
    # while parent.left or parent.right:


def print_tree(node, level=0):
    if node:
        print_tree(node.right, level=level + 1)
        print(f"{' ' * 4 * level}-> {node.value}")
        print_tree(node.left, level=level + 1)


if __name__ == "__main__":
    tree = BST()
    values = [
        4,
        7,
        2,
        9,
        3,
        0,
        14,
        12,
        8,
        4,
        -1,
        -7,
        19,
        3,
        8,
        21,
        13,
        1,
        24,
        65,
    ]
    for value in values:
        tree.insert(value)
    print_tree(tree.root)
    print(tree.find(14).right.value)
    print(tree.max_value_node(tree.root).value)
    print(tree.min_value_node(tree.root).value)
    print(tree.max_value_node(tree.root.left).value)
