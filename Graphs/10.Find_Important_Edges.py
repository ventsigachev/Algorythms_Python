"""
    The purpose of the task is to find the edges, without them a graph becomes a multi-graph.
    On the first line of input one will receive the number of nodes,
    on the second line - number of edges, and on the next N lines connected nodes.
"""


def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for c in graph[node]:
        dfs(c, graph, visited)


def main():
    nodes = int(input())
    edges = int(input())

    graph = []
    [graph.append([]) for _ in range(nodes)]

    edges_list = set()
    important_edges = []

    for _ in range(edges):
        start, end = [int(x) for x in input().split(" - ")]
        graph[start].append(end)
        graph[end].append(start)
        # adding edges in ascendant order
        edges_list.add((min(start, end), max(start, end)))

    for start, end in edges_list:
        graph[start].remove(end)
        graph[end].remove(start)

        # after removing edge, trying to reach every node in the graph, using dfs
        visited = [False] * nodes

        dfs(0, graph, visited)

        if not all(visited):
            important_edges.append((start, end))

        # returning the edge back in graph for next recursion
        graph[start].append(end)
        graph[end].append(start)

    print(important_edges)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
    
5
5
1 - 0
0 - 2
2 - 1
0 - 3
3 - 4

7
8
0 - 1
1 - 2
2 - 0
1 - 3
1 - 4
1 - 6
3 - 5
4 - 5

"""
