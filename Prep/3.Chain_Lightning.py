"""
    You are given all neighborhoods in Sofia and the distances between them. A thunderstorm is raging above the city
    with lightning strikes falling all around.
    When lightning falls, it damages all connected neighborhoods, but the damage halves with each jump (integer
    division). The lightning always jumps to a neighborhood that has the smallest distance to any neighborhood already
    damaged. Note that lightning does not necessarily fork only at its tail. Also, the same lightning cannot damage the
    same neighborhood twice. Consider the example: lightning falls on the 1st neighborhood with full force,
    then jumps to the 3rd (distance to 1st is smallest) with its damage halved. After that, the nearest one is the 2nd
    (distance from first is 10, damage also halved) and lastly, it jumps to the 4th from the 2nd (15 < 20),
    with initial damage divided by 2 and then divided by 2 again.
        1. Input
        •   The first line holds an integer n – the number of neighborhoods
        •   On the second line, you will receive the number m – the number of distances
        •   On the third line, l - the number of lightning
        •   At the next m lines, you will receive the distances: {from neighbourhood} {to neighbourhood} {distance}
        •   At the next l lines, you will receive the lightning strikes: {neighborhood} {damage}
        •   The neighborhood will always be numbered from 0 to N - 1

        2. Output
        •   Print the condition of the most heavily damaged neighborhood

        3. Constraints
        •   The number of neighborhoods will be an integer in the range [0…5000]
        •   The number of connections will be an integer in the range [0…10000]
        •   The number of lightning strikes will be an integer in the range [0…1000]
        •   Distance between neighborhoods will be a unique integer in the range [0…100000]
        •   Lightning damage will be an integer in the range [0…1000]
"""
from queue import PriorityQueue


def calc_damage(jumps, damage):
    for _ in range(jumps):
        damage //= 2

    return damage


def prim(node, damage, nodes_damages, graph):
    tree = {node}
    nodes_damages[node] += damage
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = -1, -1

        if min_edge.f in tree and min_edge.s not in tree:
            tree_node, non_tree_node = min_edge.f, min_edge.s
        elif min_edge.s in tree and min_edge.f not in tree:
            non_tree_node, tree_node = min_edge.f, min_edge.s

        if non_tree_node == -1:
            continue

        tree.add(non_tree_node)
        [pq.put(edge) for edge in graph[non_tree_node]]

        jumps[non_tree_node] = jumps[tree_node] + 1
        nodes_damages[non_tree_node] += calc_damage(jumps[non_tree_node], damage)


def result(nodes_damages):
    r = max(nodes_damages)

    print(f"The condition of the most heavily damaged neighborhood is {r}")


def main():
    class Edge:
        def __init__(self, f, s, d):
            self.f = f
            self.s = s
            self.d = d

        def __gt__(self, other):
            return self.d > other.d

    nodes = int(input())
    edges = int(input())
    levin = int(input())

    graph = {node: [] for node in range(nodes)}

    for _ in range(edges):
        first, second, distance = [int(x) for x in input().split()]
        edge = Edge(first, second, distance)
        graph[first].append(edge)
        graph[second].append(edge)

    nodes_damages = [0] * nodes

    for _ in range(levin):
        node, damage = [int(x) for x in input().split()]
        prim(node, damage, nodes_damages, graph)

    result(nodes_damages)


if __name__ == "__main__":
    main()

"""
    Possible Inputs:

5
5
2
0 1 10
1 4 20
2 4 30
0 2 35
0 3 50
0 40
4 20

10
8
3
0 1 5
1 2 4
1 3 6
2 3 3
2 5 7
2 4 2
7 6 8
7 8 1
2 100
0 200
9 100

"""
