"""
    The Graph is undirected. Nodes are numeric from 0-6.
    In this case we use list, where indexes are nodes  in graph, and sublists are connections.
"""


def depth_first_search(n, g, v, r):
    if v[n]:
        return

    v[n] = True

    for child in g[n]:
        depth_first_search(child, g, v, r)

    r.append(n)


def main():
    graph = [
        [3, 6],
        [3, 6, 4, 2, 5],
        [1, 4, 5],
        [5, 0, 1],
        [1, 2, 6],
        [2, 1, 3],
        [0, 1, 4],
    ]

    visited = [False] * len(graph)
    result = []

    for node in range(len(graph)):
        depth_first_search(node, graph, visited, result)

    if result:
        print(*result)


if __name__ == "__main__":
    main()
