from typing import Dict, List


class BidirectonalAdjacencyListGraph:
    def __init__(self) -> None:
        self.adj_list: Dict[List] = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            connected_vertices = self.adj_list[vertex]
            for connected_vertex in connected_vertices:
                self.adj_list[connected_vertex].remove(vertex)
            self.adj_list.pop(vertex)

    def __str__(self) -> str:
        str_rep = "\n"
        for key in self.adj_list.keys():
            str_rep += f"{key}: {self.adj_list[key]}\n"
        return str_rep


def bfs(grph: BidirectonalAdjacencyListGraph, vertex: int):
    # This has special code for traversing bi directional trees
    queue = [vertex]
    visited = []
    result = []
    for element in queue:
        print(queue)
        visited.append(element)
        result.append(element)
        for neighbour in grph.adj_list[element]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

    return result


if __name__ == "__main__":
    graph = BidirectonalAdjacencyListGraph()
    graph.add_vertex(vertex=4)
    graph.add_vertex(vertex=7)
    graph.add_vertex(vertex=3)
    graph.add_edge(vertex1=4, vertex2=7)
    graph.add_edge(vertex1=3, vertex2=7)
    graph.add_edge(vertex1=9, vertex2=4)
    graph.add_edge(vertex1=4, vertex2=3)
    print(graph)
    print(bfs(graph, 7))
    graph.remove_edge(vertex1=7, vertex2=3)
    graph.remove_vertex(vertex=7)
    print(graph)
    graph.add_vertex(vertex=9)
    graph.remove_edge(vertex1=9, vertex2=4)
    print(graph)
