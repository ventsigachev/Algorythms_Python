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
"""


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

    print(graph)


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
