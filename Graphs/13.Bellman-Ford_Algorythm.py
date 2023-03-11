"""
    Finds the shortest path in weighted graph, with negative edges.
        ▪ Computes the shortest paths from a source vertex to all other vertices in a weighted digraph
        ▪ Named after Richard Bellman and Lester Ford Jr., who published it in 1958 and 1956, respectively
        ▪ Can detect and report negative cycles
        ▪ Time complexity: O(VE) -> (Vertices * Edges)

        ▪ The Bellman-Ford algorithm will do V - 1 iterations, where V is the number of vertices
        ▪ For each iteration:
            ▪ For each edge in the graph (u, v, w)
            ▪ If d[v] > d[u] + w(u, v) and d[v] is visited before
            ▪ Update d[v] with d[u] + w(u, v)
            ▪ Update the prev[v] = u
        ▪ Run the algorithm one more time for each edge
        ▪ If you can update any d[v] there is a negative cycle
"""

from collections import deque


def result(distance, parent, end):
    if is_negative:
        print("Negative Cycle Detected")
        return

    path = deque()
    n = end

    while n is not None:
        path.appendleft(n)
        n = parent[n]

    print(f"The shortest path is thru nodes: {' -> '.join([str(s) for s in path])}, "
          f"with shortest distance: {distance[end]}")


def bellman_ford(graph, nodes, distance, parent):
    global is_negative

    for _ in range(nodes - 1):
        for edge in graph:
            if not distance[edge.s] == float('inf') and distance[edge.s] + edge.w < distance[edge.d]:
                distance[edge.d] = distance[edge.s] + edge.w
                parent[edge.d] = edge.s

    # checking for negative cycle
    for edge in graph:
        dist = distance[edge.s] + edge.w
        if dist < distance[edge.d]:
            is_negative = True
        return


def main():

    class Edge:
        def __init__(self, s, d, w):
            self.s = s
            self.d = d
            self.w = w

    nodes = int(input())
    edges = int(input())

    graph = []

    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split()]
        graph.append(Edge(source, destination, weight))

    start = int(input())
    end = int(input())

    distance = [float('inf')] * (nodes + 1)
    distance[start] = 0
    parent = [None] * (nodes + 1)

    bellman_ford(graph, nodes, distance, parent)
    result(distance, parent, end)


if __name__ == "__main__":
    is_negative = False
    main()


"""
    Possible Inputs:

6
8
1 2 8
1 3 10
2 4 1
3 6 2
4 3 -4
4 6 -1
6 5 -2
5 3 1
1
6

4
4
1 2 1
2 3 -1
3 4 -1
4 1 -1
1
4

If you want to visualize the graph go to https://csacademy.com/app/graph_editor/ and paste all the edges in Graph Data
column, in the upper left corner.
"""
