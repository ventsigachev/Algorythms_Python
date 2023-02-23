columns = set()
left_diagonal = set()
right_diagonal = set()


def display_matrix(matrix):
    for row in matrix:
        print(*row)
    print()


def is_not_available(row, col):
    ld = row - col
    rd = row + col
    return col in columns or ld in left_diagonal or rd in right_diagonal


def place_queen(matrix, row, col):
    matrix[row][col] = '*'
    columns.add(col)
    left_diagonal.add(row - col)
    right_diagonal.add(row + col)


def remove_queen(matrix, row, col):
    matrix[row][col] = '-'
    columns.remove(col)
    left_diagonal.remove(row - col)
    right_diagonal.remove(row + col)


def check_matrix(matrix, row=0):
    if row == 8:
        display_matrix(matrix)
        return

    for col in range(8):
        if not is_not_available(row, col):
            place_queen(matrix, row, col)
            check_matrix(matrix, row + 1)
            remove_queen(matrix, row, col)


def main():
    matrix = [['-'] * 8 for _ in range(8)]
    check_matrix(matrix)


if __name__ == "__main__":
    main()
