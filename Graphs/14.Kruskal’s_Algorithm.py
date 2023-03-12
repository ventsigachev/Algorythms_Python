"""
    If we have a weighted undirected graph, we can extract a sub-graph where all nodes (vertices) of the original graph
    are connected by edges without any cycles. This is referred to as a spanning tree. A minimum spanning tree (MST) is
    the spanning tree with the smallest weight (several MST could exist in some graphs).
    For example, a cable operator wants to connect its customers to a cable network. The homes of the customers are
    connected by streets (edges) with different lengths (weights). To find out how to connect all homes to its network
    most efficiently (the least distance covered) you need to find the MST.

    One simple algorithm to find the MST of a given graph is Kruskal’s algorithm.

    ▪ Start from forest holding all vertices and no edges
    ▪ S = all edges, ordered by weight
    ▪ F={}
    ▪ Take the smallest edge. If The edge connects different trees → add it to the forest.
    ▪ Time complexity: O(|E| * log* |E|) -> O(n * log(n))

    Input
    • On the first line you will receive e – an integer – number of edges that you have to read.
    • On the next e lines, you will receive an edge in the following format: "{firstNode}, {secondNode}, {weight}".

"""


def find_root(parent, root):
    while not root == parent[root]:
        root = parent[root]

    return root


def algoritm(graph, max_node):

    parent = [num for num in range(max_node + 1)]
    forest = []
    d = 0

    for e in sorted(graph, key=lambda x: x.w):
        first_root = find_root(parent, e.f)
        second_root = find_root(parent, e.s)
        if not first_root == second_root:
            parent[first_root] = second_root
            forest.append((e.f, e.s))
            d += e.w

    return forest, d


def result(path, distance):
    for a, b in sorted(path, key=lambda x: (x[0], x[1])):
        print(f"{a}->{b}", end=' ')

    print(f"\nThe minimum distance is: {distance}")


def main():

    class Edge:
        def __init__(self, f, s, w):
            self.f = f
            self.s = s
            self.w = w

    edges = int(input())
    graph = []
    nodes_number = 0

    for _ in range(edges):
        first, second, weight = [int(e) for e in input().split(', ')]
        graph.append(Edge(first, second, weight))

        # to find nodes number
        nodes_number = max(first, second, nodes_number)

    path, distance = algoritm(graph, nodes_number)
    result(path, distance)


if __name__ == "__main__":
    main()


"""
Possible Inputs:

11
0, 3, 9
0, 5, 4
0, 8, 5
1, 4, 8
1, 7, 7
2, 6, 12
3, 5, 2
3, 6, 8
3, 8, 20
4, 7, 10
6, 8, 7

"""
