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

    Input
    • On the first line you will receive e – an integer – number of edges that you have to read.
    • On the next e lines, you will receive an edge in the following format: "{firstNode}, {secondNode}, {weight}".

"""


def main():
    pass


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
