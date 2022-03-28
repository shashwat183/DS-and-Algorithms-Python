from collections import deque
from typing import Dict, List

# Graph Traversal on a cyclic graph would give an infinite loop.
# Use the recording visited method to prevent that
def bfs(graph: Dict, source: int):
    queue = deque()
    queue.append(source)
    result = []
    while len(queue) > 0:
        node = queue.popleft()
        result.append(node)
        for neighbour in graph[node]:
            queue.append(neighbour)

    return result


def dfs_iterative(graph: Dict, source: int):
    stack = deque()
    stack.append(source)
    result = []
    while len(stack) > 0:
        node = stack.pop()
        result.append(node)
        for neighbour in graph[node]:
            stack.append(neighbour)

    return result


def dfs_recursive(graph: Dict, node: int, result: List):
    result.append(node)
    for neighbour in graph[node]:
        dfs_recursive(graph=graph, node=neighbour, result=result)

    return result


if __name__ == "__main__":
    # graph = {1: [4, 7, 9], 3: [4], 4: [], 7: [3], 6: [], 9: [6, 11], 11: []}
    graph = {1: [4, 7, 9], 3: [], 4: [], 7: [3], 6: [], 9: [6, 11], 11: []}
    print(bfs(graph=graph, source=1))
    print(dfs_iterative(graph=graph, source=1))
    print(dfs_recursive(graph=graph, node=1, result=[]))
