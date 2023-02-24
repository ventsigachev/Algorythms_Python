"""
Area of cells in which there is a path between every two cells.
    • On the first line, you will get the number of rows.
    • On the second line, you will get the number of columns.
    • The rest of the input will be the actual matrix.

"""


class Area:
    def __init__(self, r, c, s):
        self.r = r
        self.c = c
        self.s = s


def find_areas(matrix, row, col):

    if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]):
        return 0
    if not matrix[row][col] == '-':
        return 0

    matrix[row][col] = 'a'

    result = 1
    result += find_areas(matrix, row - 1, col)
    result += find_areas(matrix, row + 1, col)
    result += find_areas(matrix, row, col - 1)
    result += find_areas(matrix, row, col + 1)

    return result


def main():
    rows = int(input())
    cols = int(input())
    matrix = [list(input()) for _ in range(rows)]

    areas = []

    for row in range(rows):
        for col in range(cols):
            result = find_areas(matrix, row, col)
            if result:
                areas.append(Area(row, col, result))

    for position, a in enumerate(sorted(areas, key=lambda x: x.s, reverse=True), start=1):
        print(f"Area #{position} at ({a.r}, {a.c}), size: {a.s}")


if __name__ == "__main__":
    main()


"""
Possible input
5
10
*--*---*--
*--*---*--
*--*****--
*--*---*--
*--*---*--
"""
