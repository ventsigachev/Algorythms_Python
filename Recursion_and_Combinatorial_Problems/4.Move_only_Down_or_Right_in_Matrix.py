"""
    Define the matrix with inputs,
    and find all possible roads to the last cell, from first one.
    It is not necessarily to create real matrix!

"""


def find_all_roads(rows, cols, row=0, col=0):
    """ Bottom cases:"""
    if row == rows or col == cols:
        #  out of matrix
        return 0

    if row == rows - 1 and col == cols - 1:
        #  in the last cell
        return 1

    """ Recursion itself:"""
    roads = find_all_roads(rows, cols, row + 1, col)   # moving Right
    roads += find_all_roads(rows, cols, row, col + 1)  # moving Down

    return roads


def main():
    rows = int(input())
    cols = int(input())

    print(find_all_roads(rows, cols))


if __name__ == "__main__":
    main()
