"""
    We are given a directed graph. We are given also a set of pairs of vertices. Find the shortest distance between each
    pair of vertices or -1 if there is no path connecting them.
    On the first line, you will get N, the number of vertices in the graph.
    On the second line, you will get P, the number of pairs between which to find the shortest distance.
    On the next N lines will be the edges of the graph and on the next P lines, the pairs.
"""


def main():
    nodes = int(input())
    edges = int(input())

    graph = []
    [graph.append(None) for _ in range(nodes + 1)]

    for _ in range(nodes):
        parent, children = input().split(':')
        parent = int(parent)
        children = list(map(int, children.split())) if children else ""
        if children:
            graph[parent] = children

    print(graph)
    
    pairs = []
    for _ in range(edges):
        a, b = input().split('-')
        pairs.append((int(a), int(b)))

    print(pairs)


if __name__ == "__main__":
    main()


"""
 Possible Inputs:
 
2
2
1:2
2:
1-2
2-1

8
4
1:4
2:4
3:4 5
4:6
5:3 7 8
6:
7:8
8:
1-6
1-5
5-6
5-8

9
8
11:4
4:12 1
1:12 21 7
7:21
12:4 19
19:1 21
21:14 31
14:14
31:
11-7
11-21
21-4
19-14
1-4
1-11
31-21
11-14

"""
