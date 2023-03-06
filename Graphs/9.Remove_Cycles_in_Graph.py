"""
    You are given an undirected multi-graph. Remove a minimal number of edges to make the graph acyclic (to break all
    cycles). As a result, print the number of edges removed and the removed edges. If several edges can be removed to
    break a certain cycle, remove the smallest of them in ascendant order.
"""


def main():
    n = int(input())
    graph = {}

    for _ in range(n):
        node, vertex = input().split(" -> ")
        nodes = vertex.split()
        graph[node] = nodes

    print(graph)


if __name__ == "__main__":
    main()


"""
Possible inputs:

8
1 -> 2 5 4
2 -> 1 3
3 -> 2 5
4 -> 1
5 -> 1 3
6 -> 7 8
7 -> 6 8
8 -> 6 7

14
K -> X J
J -> K N
N -> J X L M
X -> K N Y
M -> N I
Y -> X L
L -> N I Y
I -> M L
A -> Z Z Z
Z -> A A A
F -> E B P
E -> F P
P -> B F E
B -> F P

"""