"""
    Program to check whether a directed graph is acyclic or holds any cycles.
    The input ends with "End" line.
    We use depth-first search(DFS).
"""


def dfs(node, graph, visited, set_for_cycle=None):
    if not set_for_cycle:
        set_for_cycle = set()

    if node in set_for_cycle:
        raise Exception

    if node in visited:
        return

    visited.append(node)
    set_for_cycle.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, set_for_cycle)

    set_for_cycle.remove(node)


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

    visited = []

    try:
        for node in graph:
            dfs(node, graph, visited)
        print("The Graph is Acyclic")

    except Exception as e:
        e = "The Graph is Cyclic"
        print(e)


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
