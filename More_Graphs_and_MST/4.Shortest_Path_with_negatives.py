"""
   The task is to find the shortest path in a graph from S vertex to D vertex.
   However, edges might have negative weights.
   Input
    • On the first line, you will receive an integer – n – number of nodes.
    • On the second line, you will receive an integer – e – number of edges.
    • On the next e lines, you will receive edges in the following format: "{source} {destination} {weight}".
    • On the next line, you will receive an integer – source – the start of the path.
    • On the last line, you will receive an integer – destination – end of the path.

"""


def results(parents, distances, end):
    if is_negative:
        print("There is a negative cycle in the graph")
        return

    path = []
    node = end

    while node is not None:
        path.append(node)
        node = parents[node]

    print(f"The shortest distance in graph is {distances[end]}, thru {' -> '.join([str(s) for s in reversed(path)])} "
          f"nodes")


def algorithm(nodes, graph, start, end):

    distances = [float('inf')] * (nodes + 1)
    distances[start] = 0
    parents = [None] * (nodes + 1)
    global is_negative

    for _ in range(nodes - 1):
        for s, d, w in graph:
            if distances[s] == float('inf'):
                continue
            destination_node_distance = distances[s] + w
            if destination_node_distance < distances[d]:
                distances[d] = destination_node_distance
                parents[d] = s

    for s, d, w in graph:
        d_n_d = distances[s] + w
        if d_n_d < distances[d]:
            is_negative = True

    results(parents, distances, end)


def main():
    nodes = int(input())
    edges = int(input())

    graph = []

    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split()]
        graph.append((source, destination, weight))

    start = int(input())
    end = int(input())

    algorithm(nodes, graph, start, end)


if __name__ == "__main__":
    is_negative = False
    main()


"""
    Possible Inputs:
 
5
8
1 2 -1
1 3 4
2 3 3
2 4 2
2 5 2
4 2 1
4 3 5
5 4 -3
1
4

5
8
1 2 -1
1 3 4
2 3 3
2 4 2
2 5 2
4 2 -1
4 3 5
5 4 -3
1
4

"""