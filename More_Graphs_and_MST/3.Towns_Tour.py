"""
    Visit every node in the graph as cheap as possible.

    Input
        • On the first line, you will be given the number of the nodes.
        • On the second line, you will be given the number of edges (n).
        • On the next n lines, you will be given a connection in the format: "{first} - {second} - {cost}".
"""


def main():

    nodes = int(input())
    edges = int(input())

    graph = []

    for _ in range(edges):
        first, second, cost = [int(x) for x in input().split(" - ")]
        graph.append((first, second, cost))

    print(graph)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
    
4
5
0 - 1 - 10
0 - 2 - 6
0 - 3 - 5
1 - 3 - 15
2 - 3 - 4

"""
