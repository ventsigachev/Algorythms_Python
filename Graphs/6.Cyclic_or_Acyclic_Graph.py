"""
    Program to check whether a directed graph is acyclic or holds any cycles.
    The input ends with "End" line.
    We use depth-first search(DFS).
"""


def main():
    graph = {}

    while True:
        line = input()
        if line == "End":
            break
        node_a, node_b = line.split("-")
        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []
        graph[node_a].append(node_b)

    print(graph)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
    
C-G
End

A-F
F-D
D-A
End

E-Q
Q-P
P-B
End

K-J
J-N
N-L
N-M
M-I
End

"""