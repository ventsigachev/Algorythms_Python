"""
    We are in a rectangular room. On opposite sides of the room, there are sets of n cables (n < 1000). The cables are
    indexed from 1 to n. On each side of the room, there is a permutation of the cables,
    e.g. on one side we always have ordered {1, 2, 3, 4, 5},
    and on the other side, we have some permutation {5, 1, 3, 4, 2}.
    We are trying to connect each cable from one side with the corresponding cable on the other side –
    connect 1 with 1, 2 with 2, etc. The cables are straight and should not overlap!
    The task is to find the maximum number of pairs we can connect given the restrictions above.

"""


def main():
    inputs = [int(c) for c in input().split()]
    size = len(inputs) + 1
    cables = [x for x in range(1, size)]

    matrix = []
    [matrix.append([0] * size) for _ in range(size)]

    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
    
2 5 3 8 7 4 6 9 1

4 3 2 1

1 2 3

"""
