"""
Area of cells in which there is a path between every two cells.
    • On the first line, you will get the number of rows.
    • On the second line, you will get the number of columns.
    • The rest of the input will be the actual matrix.

"""


class Area:
    def __init__(self, p):
        self.positions = p


def find_areas(matrix, row, col):

    if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]):
        return False
    if not matrix[row][col] == '-':
        return False

    matrix[row][col] = 'a'

    positions.append((row, col))

    find_areas(matrix, row - 1, col)
    find_areas(matrix, row + 1, col)
    find_areas(matrix, row, col - 1)
    find_areas(matrix, row, col + 1)

    return True


def main():
    global positions

    rows = int(input())
    cols = int(input())
    matrix = [list(input()) for _ in range(rows)]

    areas = []

    for row in range(rows):
        for col in range(cols):
            result = find_areas(matrix, row, col)
            if result:
                areas.append(Area(positions))
                positions = []

    for p, area in enumerate(areas, start=1):
        print(f"Area #{p} with {tuple(x for x in area.positions)} "
              f"positions in Matrix, contains {len(area.positions)} Matrix cells")

    for p, area in enumerate(areas, start=1):
        for t in area.positions:
            r, c = t
            matrix[int(r)][int(c)] = p

    print('\nThe Matrix: \n')
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    positions = []
    main()


"""
Possible inputs:

5
10
*--*---*--
*--*---*--
*--*****--
*--*---*--
*--*---*--

4
9
---*---*-
---*---*-
---*---*-
----*-*--

"""
