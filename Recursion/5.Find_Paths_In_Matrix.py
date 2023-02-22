def invalid_boundaries(m, r, c):
    if r < 0 or c < 0 or r >= len(m) or c >= len(m[0]):
        return True


def exit_checking(m, r, c):
    if m[r][c] == "e":
        return True


def wall_checking(m, r, c):
    if m[r][c] == "*":
        return True


def paths(matrix, direction="", path=None, row=0, col=0):
    if path is None:
        path = []

    if invalid_boundaries(matrix, row, col):
        return

    if wall_checking(matrix, row, col):
        return

    if matrix[row][col] == 'visited':
        return

    path.append(direction)

    if exit_checking(matrix, row, col):
        print("".join(path))
        path.pop()
        return

    matrix[row][col] = 'visited'

    paths(matrix, "D", path, row + 1, col)
    paths(matrix, "U", path, row - 1, col)
    paths(matrix, "R", path, row, col + 1)
    paths(matrix, "L", path, row, col - 1)

    matrix[row][col] = '-'

    path.pop()


def main():
    r = int(input())

    matrix = []

    for _ in range(r):
        matrix.append(list(input()))

    paths(matrix)


if __name__ == "__main__":
    main()


"""
Possible inputs:

3
---
-*-
--e ,

3
-**-e
-----
*****

"""
