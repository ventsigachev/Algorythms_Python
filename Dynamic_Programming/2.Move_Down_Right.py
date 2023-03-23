"""
    Given a matrix of N by M cells filled with positive integers, find the path from top left to bottom right with the
    highest sum of cells, by moving only down or right.
    You are given a matrix of numbers
        ▪ Find the path with the largest sum
        ▪ Start → top left
        ▪ End → bottom right
        ▪ Move only right or down
"""


def main():
    rows = int(input())
    cols = int(input())

    matrix = []

    for _ in range(rows):
        matrix.append([int(x) for x in input().split()])


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
    
3
3
1 1 1
1 1 1
1 1 1

3
3
1 0 6
8 3 7
2 4 9

8
7
2 6 1 8 9 4 2
1 8 0 3 5 6 7
3 4 8 7 2 1 8
0 9 2 8 1 7 9
2 7 1 9 7 8 2
4 5 6 1 2 5 6
9 3 5 2 8 1 9
2 3 4 1 7 2 8

"""