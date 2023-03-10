"""
    Dijkstra's algorithm finds the shortest path from given vertex to all other vertices in a directed / undirected
    weighted graph. First described by Edsger W. Dijkstra in 1956. Assumptions:
        ▪ Weights on edges are non-negative, works only with positive numbers.
        ▪ Edges can be directed or not.
        ▪ Weights do not have to be distances.
        ▪ The shortest path is not necessarily unique.
        ▪ Not all edges need to be reachable.
        ▪ Uses priority queue instead of queue.

    Task Description
        Find the shortest path between two nodes in a weighted graph.
        Dijkstra’s algorithm is one of the most famous ones that solve this task, by implementing the optimized
        version of Dijkstra’s algorithm using a priority queue.

        Input
            • On the first line you will receive an integer – e – number of edges.
            • On the next e lines, you will receive an edge in the following format: "{start}, {end}, {weight}".
            • On the next line, you will receive a start node.
            • On the last line, you will receive an end node.
        Output
            • Print the cost of the shortest path.
            • Print all nodes that form the shortest path.
            • If the end node can’t be reached from the start node, then you have to print: "There is no such path."

"""

from queue import PriorityQueue


def main():
    class Edge:
        def __init__(self, s, d, w):
            self.s = s
            self.d = d
            self.w = w

    edges = int(input())
    graph = {}

    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split(', ')]
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []

        graph[source].append(Edge(source, destination, weight))

    start = int(input())
    end = int(input())

    max_node = max(graph.keys())
    distance = [float('inf')] * (max_node + 1)
    parent = [None] * (max_node + 1)

    distance[start] = 0

    pq = PriorityQueue()

    pq.put((0, start))

    while not pq.empty():
        min_distance, node = pq.get()
        if node == end:
            break
        for edge in graph[node]:
            new_distance = min_distance + edge.w
            if new_distance < distance[edge.d]:
                distance[edge.d] = new_distance
                parent[edge.d] = node
                pq.put((new_distance, edge.d))

    print(distance[end])


if __name__ == "__main__":
    main()


"""
    Possible Inputs
    
18
0, 6, 10
0, 8, 12
6, 4, 17
6, 5, 6
8, 5, 3
5, 4, 5
5, 11, 33
8, 2, 14
2, 11, 9
2, 7, 15
4, 1, 20
4, 11, 11
11, 1, 6
11, 7, 20
1, 9, 5
1, 7, 26
7, 9, 3
3, 10, 7
0
9

18
0, 6, 10
0, 8, 12
6, 4, 17
6, 5, 6
8, 5, 3
5, 4, 5
5, 11, 33
8, 2, 14
2, 11, 9
2, 7, 15
4, 1, 20
4, 11, 11
11, 1, 6
11, 7, 20
1, 9, 5
1, 7, 26
7, 9, 3
3, 10, 7
0
10

"""
