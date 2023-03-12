"""
    If we have a weighted undirected graph, we can extract a sub-graph where all nodes (vertices) of the original graph
    are connected by edges without any cycles. This is referred to as a spanning tree. A minimum spanning tree (MST) is
    the spanning tree with the smallest weight (several MST could exist in some graphs).
    For example, a cable operator wants to connect its customers to a cable network. The homes of the customers are
    connected by streets (edges) with different lengths (weights). To find out how to connect all homes to its network
    most efficiently (the least distance covered) you need to find the MST.
    One simple algorithm to find the MST of a given graph is Prim’s algorithm.

    Given a graph G(V, E) find the minimum spanning forest T(V', E'). Attach to the tree T the starting node.
    While smallest edge exists, attach to T the smallest possible edge from G without creating a cycle in T.
    Use the smallest edge (u, v), such that u ∈ T and v ∉ T.
        ▪ Start from the initial node A
        ▪ Enqueue all edges from A to other graph nodes: AB, AC, AD
        ▪ Spanning tree = {A}
        ▪ Priority queue = {AB = 4}, {AC = 5}, {AD = 9}

    Input
    • On the first line, you will receive e – an integer – number of edges that you have to read.
    • On the next e lines, you will receive an edge in the following format: "{firstNode}, {secondNode}, {weight}".

"""


def main():
    pass


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
    
11
0, 2, 5
2, 4, 7
4, 5, 12
0, 1, 4
1, 3, 2
0, 3, 9
2, 3, 20
3, 4, 8
6, 7, 8
6, 8, 10
7, 8, 7

"""
