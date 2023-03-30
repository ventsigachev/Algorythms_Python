"""
    You will be given the stories in the following format on a single line until the command "End" is received.
        {preStory} -> {postStory1} {postStory2} {postStory n-1}
    You have to read the stories data and then print the stories in the correct order,
    according to the description above. Keep in mind that the structure above represents relation in which any story
    can be preStory or postStory in different input lines.
    Input
        •On a single line, the input in the above format until the "End" command is received.
    Output
        •On a single line print the stories in the correct order, separated by spaces.
        •The output priority, if there are more than one story without pre story, should be in the order of the input.
    Constraints
        •All stories will be valid and also can contain any ASCII symbol except space.
        •The input will always end with "End" line.
"""


def dfs(n, g, v, r):

    if n in v:
        return

    v.add(n)
    for c in g[n]:
        dfs(c, g, v, r)

    r.append(n)


def printing_res(result):

    print("The story order is:")
    # print(*reversed(result))
    print(*result[::-1])


def main():
    graph = {}

    while True:
        line = input()
        if line == "End":
            break

        node, children_str = [s.strip() for s in line.split("->")]
        children = children_str.split()
        graph[node] = children

    visited = set()
    result = []
    for node in graph:
        dfs(node, graph, visited, result)

    printing_res(result)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
   
Mort -> Time Space
Time -> Future Robot
Space -> Metro
Future -> Space Metro
Robot -> Future
Metro ->
End

"""
