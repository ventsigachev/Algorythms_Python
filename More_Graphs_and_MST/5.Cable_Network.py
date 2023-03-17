"""
    A cable networking company plans to extend its existing cable network by connecting as many customers as possible,
    within a fixed budget limit. The company has calculated the cost of building some prospective connections.
    You are given the existing cable network (a set of customers and connections between them), along with the estimated
    connection costs between some pairs of customers and prospective customers. A customer can only be connected to the
    network, via a direct connection, with an already connected customer.

    The task is to connect as many customers as possible, within the existing budget.

    Input
        • On the first line, you will receive an integer – budget.
        • On the second line, you will receive an integer – n – number of nodes.
        • On the third line, you will receive an integer – e – number of edges.
        • On the next e lines, you will receive edges in the following format: "{first} {second} {weight} {connected}".
"""
from queue import PriorityQueue


def prims_algorithm(graph, connected, budget):
    pq = PriorityQueue()
    budget_used = 0

    for node in connected:
        for edge in graph[node]:
            pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_connected_node = None

        if min_edge.f in connected and min_edge.s not in connected:
            non_connected_node = min_edge.s
        elif min_edge.f not in connected and min_edge.s in connected:
            non_connected_node = min_edge.f

        if not non_connected_node:
            continue

        if budget_used + min_edge.w > budget:
            break

        budget_used += min_edge.w
        connected.add(non_connected_node)

        for edge in graph[non_connected_node]:
            pq.put(edge)

    print(budget_used)


def main():

    class Edge:
        def __init__(self, f, s, w):
            self.f = f
            self.s = s
            self.w = w

        def __gt__(self, other):
            return self.w > other.w

    budget = int(input())
    nodes = int(input())
    edges = int(input())

    graph = []
    [graph.append([]) for _ in range(nodes)]

    connected = set()

    for _ in range(edges):
        edge = input().split()
        first, second, weight = int(edge[0]), int(edge[1]), int(edge[2])
        graph[first].append(Edge(first, second, weight))
        graph[second].append(Edge(first, second, weight))

        if len(edge) == 4:
            connected.add(first)
            connected.add(second)

    prims_algorithm(graph, connected, budget)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:

20
9
15
1 4 8
4 0 6 connected
1 7 7
4 7 10
4 8 3
7 8 4
0 8 5 connected
8 6 9
8 3 20 connected
0 5 4
0 3 9 connected
6 3 8
6 2 12
5 3 2
3 2 14 connected

7
4
5
0 1 9
0 3 4 connected
3 1 6
3 2 11 connected
1 2 5

20
8
16
0 1 4
0 2 5
0 3 1 connected
1 2 8
1 3 2
2 3 3
2 4 16
2 5 9
3 4 7
3 5 14
4 5 12
4 6 22
4 7 9
5 6 6
5 7 18
6 7 15

"""