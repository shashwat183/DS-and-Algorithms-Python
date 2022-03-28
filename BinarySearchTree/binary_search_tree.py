from typing import Union, List


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

    def bfs(self) -> List[int]:
        queue = []
        results = []
        queue.append(self.root)
        for element in queue:
            if element:
                results.append(element.value)
                queue.append(element.left)
                queue.append(element.right)

        return results

    def dfs_pre_order(self) -> List[int]:
        results = []

        # Recursive function to traverse the tree.
        # This creates a call STACK and essentially that
        # STACK allows us to do DFS.
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self) -> List[int]:
        results = []

        # Recursive function to traverse the tree.
        # This creates a call STACK and essentially that
        # STACK allows us to do DFS.
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self) -> List[int]:
        results = []

        # Recursive function to traverse the tree.
        # This creates a call STACK and essentially that
        # STACK allows us to do DFS.
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

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
    print(tree.bfs())
    print(tree.dfs_pre_order())
    print(tree.dfs_post_order())
    print(tree.dfs_in_order())
