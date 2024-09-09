# Build Graph

from collections import defaultdict

def build_graph(edges: list[list[int]]):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)

    return graph