"""
    We have a set of towns and some of them are connected by direct paths. Each path has a coefficient of reliability
    (in percentage): the chance to pass without incidents.
    Your goal is to compute the most reliable path between two given nodes. Assume all percentages will be integer
    numbers and round the result to the second digit after the decimal separator.
    Input
    • On the first line, you will receive an integer – n – number of nodes.
    • On the second line, you will receive an integer – e – number of edges.
    • On the next e lines, you will receive edges in the following format: "{first} {second} {weight}".
    • On the next line, you will receive an integer – source – starting of the path.
    • On the last line, you will receive an integer – destination – end of the path.

    In this case I use PriorityQueue with negative numbers, to get the max number from the queue.
"""
from queue import PriorityQueue


def algorithm(graph, start, end, nodes):
    pq = PriorityQueue()
    pq.put((-100, start))

    priority = [float('-inf')] * nodes
    priority[start] = 100
    parent = [None] * nodes

    while not pq.empty():
        max_reliability, node = pq.get()
        if node == end:
            break
        for edge in graph[node]:
            child = edge.s if edge.f == node else edge.f
            n_reliability = -max_reliability * edge.w / 100
            if n_reliability > priority[child]:
                priority[child] = n_reliability
                parent[child] = node
                pq.put((-n_reliability, child))


def main():

    class Edge:
        def __init__(self, f, s, w):
            self.f = f
            self.s = s
            self.w = w

    nodes = int(input())
    edges = int(input())

    graph = []
    [graph.append([]) for _ in range(nodes)]

    for _ in range(edges):
        first, second, weight = [int(x) for x in input().split()]
        edge = Edge(first, second, weight)
        graph[first].append(edge)
        graph[second].append(edge)

    start = int(input())
    end = int(input())

    algorithm(graph, start, end, nodes)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:

7
10
0 3 85
0 4 88
3 1 95
3 5 98
4 5 99
4 2 14
5 1 5
5 6 90
1 6 100
2 6 95
0
6

4
4
0 1 94
0 2 97
2 3 99
1 3 98
0
1

"""
