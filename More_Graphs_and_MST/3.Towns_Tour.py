"""
    Visit every node in the graph as cheap as possible.

    Input
        • On the first line, you will be given the number of the nodes.
        • On the second line, you will be given the number of edges (n).
        • On the next n lines, you will be given a connection in the format: "{first} - {second} - {cost}".
"""


def find_root(parent, node):
    while not node == parent[node]:
        node = parent[node]
    return node


def main():

    nodes = int(input())
    edges = int(input())

    graph = []

    for _ in range(edges):
        first, second, cost = [int(x) for x in input().split(" - ")]
        graph.append((first, second, cost))

    parent = [num for num in range(nodes)]
    total_cost = 0

    for f, s, c in sorted(graph, key=lambda x: x[2]):
        first_root = find_root(parent, f)
        second_root = find_root(parent, s)

        if first_root == second_root:
            continue
        parent[first_root] = second_root
        total_cost += c

    print(f"Total cost is: {total_cost}")


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
