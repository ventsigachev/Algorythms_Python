"""
    The purpose of the task is to find the edges, without them a graph becomes a multi-graph.
    On the first line of input one will receive the number of nodes,
    on the second line - number of edges, and on the next N lines connected nodes.
"""


def main():
    nodes = int(input())
    edges = int(input())

    graph = []
    [graph.append([]) for _ in range(nodes)]

    edges_list = set()

    for _ in range(edges):
        start, end = [int(x) for x in input().split(" - ")]
        graph[start].append(end)
        graph[end].append(start)
        # adding edges in ascendant order
        edges_list.add((min(start, end), max(start, end)))

    print(graph)
    print(edges_list)


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
