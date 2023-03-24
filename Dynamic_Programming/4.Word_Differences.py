"""
    Write a program that finds all the differences between two strings. You have to determine the smallest
    set of deletions and insertions to make the first string equal to the second.
    Finally, you have to print the count of the minimum insertions and deletions.
        Input
            • You will receive the two strings on separate lines
        Output
            • Print the minimum amount of deletions and insertions
"""


def main():
    f_str = input()
    s_str = input()

    matrix = []

    for _ in range(len(f_str) + 1):
        matrix.append([0] * (len(s_str) + 1))
    for col in range(1, len(s_str) + 1):
        matrix[0][col] = col
    for row in range(1, len(f_str) + 1):
        matrix[row][0] = row

    r = len(f_str) + 1
    c = len(s_str) + 1

    for row in range(1, r):
        for col in range(1, c):
            if f_str[row - 1] == s_str[col - 1]:
                matrix[row][col] = matrix[row - 1][col - 1]
            else:
                matrix[row][col] = min(matrix[row][col - 1], matrix[row - 1][col]) + 1

    result = matrix[r - 1][c - 1]
    print(f"The minimum amount of deletions and insertions are: {result}")


if __name__ == "__main__":
    main()


"""
    Possible Inputs:

YMCA
HMBB

JFEIOWHGOW
GHEWQHFEWQ

"""
