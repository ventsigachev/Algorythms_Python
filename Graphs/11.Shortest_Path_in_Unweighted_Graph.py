"""
    You will be given a graph from the console.
    Your task is to find the shortest path and print it back on the console.
    The first line will be the number of Nodes - N, the second one - the number of Edges - E,
    then on each E line - the edge in form {destination} – {source}.
    On the last two lines, you will read the start node and the end node.

    The better solution is to use breath-first search(BTF).
"""
from collections import deque


def main():
    nodes = int(input())
    edges = int(input())

    graph = []
    [graph.append([]) for _ in range(nodes + 1)]

    for _ in range(edges):
        source, destination = [int(x) for x in input().split()]
        graph[source].append(destination)

    start = int(input())
    end = int(input())

    visited = [False] * (nodes + 1)
    parent_nodes = [None] * (nodes + 1)

    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for n in graph[node]:
            if visited[n]:
                continue
            visited[n] = True
            queue.append(n)
            parent_nodes[n] = node

    print(parent_nodes)


if __name__ == "__main__":
    main()


"""
Possible Inputs:

8
10
1 2
1 4
2 3
4 5
5 8
5 6
5 7
5 8
6 7
7 8
1
7

11
11
1 5
1 4
5 7
7 8
8 2
2 3
3 4
4 1
6 2
9 10
11 9
6
3

"""
