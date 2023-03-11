"""
    Finds the shortest path in weighted graph, with negative edges.
        ▪ Computes the shortest paths from a source vertex to all other vertices in a weighted digraph
        ▪ Named after Richard Bellman and Lester Ford Jr., who published it in 1958 and 1956, respectively
        ▪ Can detect and report negative cycles
        ▪ Time complexity: O(VE) -> (Vertices * Edges)
"""


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

    print(graph)


if __name__ == "__main__":
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

"""
