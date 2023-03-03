"""
    Traversing a graph means to visit each of its nodes exactly once.
    The order of visiting nodes may vary on the traversal algorithm.
        ▪ Depth-First Search (DFS)
            ▪ Visit node's successors first
            ▪ Usually implemented by recursion
"""


def depth_first_search(n, g, v):
    if n in v:
        return

    v.add(n)

    for child in g[n]:
        depth_first_search(child, g, v)

    print(n, end=" ")


def main():
    graph = {

        1: [19, 21, 14],
        19: [7, 12, 31, 21],
        7: [1],
        12: [],
        31: [21],
        21: [14],
        14: [23, 6],
        23: [21],
        6: [],

    }

    visited = set()

    for node in graph:
        depth_first_search(node, graph, visited)


if __name__ == "__main__":
    main()

"Nodes are printed, in order they moved out from the stack"
