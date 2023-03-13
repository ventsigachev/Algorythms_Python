"""
    We are given a directed graph. We are given also a set of pairs of vertices. Find the shortest distance between each
    pair of vertices or -1 if there is no path connecting them.
    On the first line, you will get N, the number of vertices in the graph.
    On the second line, you will get P, the number of pairs between which to find the shortest distance.
    On the next N lines will be the edges of the graph and on the next P lines, the pairs.
"""
from collections import deque


def bfs(graph, pairs):

    for pair in pairs:
        source, destination = pair
        queue = deque([source])
        visited = {source}
        parent = {source: None}

        while queue:
            node = queue.popleft()
            if node == destination:
                break
            for child in graph[node]:
                if child in visited:
                    continue

                queue.append(child)
                visited.add(child)
                parent[child] = node

        path = deque()
        node = destination

        while node:
            if node not in parent:
                break
            path.appendleft(node)
            node = parent[node]

        print(f"From {source} to {destination}, the path is: {', '.join([str(x) for x in path])}" if len(path) > 1 else
              f"From {source} to {destination} there is no path")


def main():
    nodes = int(input())
    edges = int(input())

    graph = {}

    for _ in range(nodes):
        parent, children = input().split(':')
        parent = int(parent)
        children = list(map(int, children.split())) if children else []
        graph[parent] = children

    pairs = []
    for _ in range(edges):
        a, b = input().split('-')
        pairs.append((int(a), int(b)))

    bfs(graph, pairs)


if __name__ == "__main__":
    main()


"""
 Possible Inputs:
 
2
2
1:2
2:
1-2
2-1

8
4
1:4
2:4
3:4 5
4:6
5:3 7 8
6:
7:8
8:
1-6
1-5
5-6
5-8

9
8
11:4
4:12 1
1:12 21 7
7:21
12:4 19
19:1 21
21:14 31
14:14
31:
11-7
11-21
21-4
19-14
1-4
1-11
31-21
11-14

"""
