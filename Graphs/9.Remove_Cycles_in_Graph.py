"""
    You are given an undirected multi-graph. Remove a minimal number of edges to make the graph acyclic (to break all
    cycles). As a result, print the number of edges removed and the removed edges. If several edges can be removed to
    break a certain cycle, remove the smallest of them in ascendant order.
    For ability to remove edges, create a list of tuples, sorted in ascendant order.
"""


def dfs(node, end, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for vertex in graph[node]:
        dfs(vertex, end, graph, visited)


def check_paths(start, end, graph):
    visited = set()

    dfs(start, end, graph, visited)
    
    return end in visited


def main():
    n = int(input())
    graph = {}
    edges = []

    for _ in range(n):
        node, vertex = input().split(" -> ")
        nodes = vertex.split()
        graph[node] = nodes
        for edge in nodes:
            edges.append((node, edge))

    edges = sorted(edges, key=lambda x: (x[0], x[1]))

    # let check for cycles by removing edges from graph
    for start, end in edges:
        if end not in graph[start] or start not in graph[end]:
            continue

        graph[start].remove(end)
        graph[end].remove(start)

        # now check if there is a different path from start to end in graph, using dfs
        # this check returns boolean for path existence
        # if there is a path, graph is cycled, so remove option above persists
        if check_paths(start, end, graph):
            print(start, end, sep=" - ")
        # if there is no other path, return the above edge to graph
        else:
            graph[start].append(end)
            graph[end].append(start)


if __name__ == "__main__":
    main()


"""
Possible inputs:

8
1 -> 2 5 4
2 -> 1 3
3 -> 2 5
4 -> 1
5 -> 1 3
6 -> 7 8
7 -> 6 8
8 -> 6 7

14
K -> X J
J -> K N
N -> J X L M
X -> K N Y
M -> N I
Y -> X L
L -> N I Y
I -> M L
A -> Z Z Z
Z -> A A A
F -> E B P
E -> F P
P -> B F E
B -> F P

"""