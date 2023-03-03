"""
    The Graph consists multiple components, some of which are connected nodes.
"""


def depth_first_search(n, g, v, component):

    if n in v:
        return

    v.add(n)

    for c in g[n]:
        depth_first_search(c, g, v, component)

    component.append(n)
    return component


def main():
    numbers_of_nodes = int(input())
    graph = []
    for node in range(numbers_of_nodes):
        line = input()
        children = [int(c) for c in line.split()] if line else []
        graph.append(children)

    visited = set()

    all_components = []

    for node in range(numbers_of_nodes):
        component = []
        depth_first_search(node, graph, visited, component)

        if component:
            all_components.append(component)

    for n, cs in enumerate(all_components):
        if len(cs) > 1:
            print(f"Connected Component # {n + 1} with nodes: {' '.join([str(x) for x in cs])}")
        else:
            print(f"Component # {n + 1}: with node: {' '.join([str(x) for x in cs])}")


if __name__ == "__main__":
    main()


"""
Possible Inputs:

9
3 6
3 4 5 6
8
0 1 5
1 6
1 3
0 1 4

2

"""
