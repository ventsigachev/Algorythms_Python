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
    second_matrix = []

    for _ in range(rows):
        matrix.append([int(x) for x in input().split()])
        second_matrix.append([0] * cols)

    second_matrix[0][0] = matrix[0][0]
    for col in range(1, cols):
        second_matrix[0][col] = second_matrix[0][col - 1] + matrix[0][col]

    for row in range(1, rows):
        second_matrix[row][0] = second_matrix[row - 1][0] + matrix[row][0]

    for row in second_matrix:
        print(row)


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