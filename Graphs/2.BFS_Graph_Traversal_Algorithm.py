"""
    Traversing a graph means to visit each of its nodes exactly once.
    The order of visiting nodes may vary on the traversal algorithm.
        ▪ Breadth-First Search (BFS). We use queue in this case.
            ▪ Nearest nodes visited first
            ▪ Implemented with a QUEUE
        First visits the neighbor nodes, then the neighbors of neighbors, then their neighbors, etc.
        We add the current node in the queue.
        In this case the graph is DIRECTED with numeric nodes.
"""
from collections import deque


def breadth_first_search(n, g, v, r):
    if n in v:
        return

    queue = deque([n])
    v.add(n)

    while queue:
        current_node = queue.popleft()
        r.append(current_node)
        for child in g[current_node]:
            if child not in v:
                v.add(child)
                queue.append(child)


def main():
    graph = {
        7: [19, 21, 14],
        19: [1, 12, 31, 21],
        1: [7],
        12: [],
        31: [21],
        21: [14],
        14: [6, 23],
        6: [],
        23: [21],
    }

    visited = set()
    result = []

    for node in graph:
        breadth_first_search(node, graph, visited, result)

    if result:
        print(*result)


if __name__ == "__main__":
    main()


"""
    The Graph is directed and has layers: Top to Bottom -> I layer 7; II layer 19, 21, 14; III layer 1, 12, 31, 6, 23.
    The Graph is with one component. 
"""