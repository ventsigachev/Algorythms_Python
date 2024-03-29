"""
    You will be given two sequences of integers representing two timeline versions. You need to extract from both
    sequences the single correct timeline that can be retrieved by finding the longest subsequence of equal integers
    from both timelines and also finding its length.
        Input
        •   The first line integers represent the first timeline separated by spaces.
        •   The second line integers represent the second timeline separated by spaces.

        Output
        •   On the first line print the correct timeline, if there are more than one optimal timeline print the rightmost.
        •   On the second line print the length of that timeline.

        Constraints
        •   All numbers will be valid integers.
        •   The length of the timelines will be between [1…5000].

"""


def result_representation(m, f, s):
    r = len(m) - 1
    c = r
    result = []

    while r > 0 and c > 0:

        if f[r - 1] == s[c - 1]:
            result.append(f[r - 1])
            r -= 1
            c -= 1

        elif m[r - 1][c] > m[r][c - 1]:
            r -= 1

        else:
            c -= 1

    result.reverse()

    print(f"The correct timeline is { ' '.join(result) }")
    print(f"The length of that timeline is { len(result) }")


def main():
    first = input().split()
    second = input().split()

    rows = len(first) + 1
    cols = len(second) + 1
    matrix = []
    for _ in range(rows):
        matrix.append([0] * cols)

    for row in range(1, rows):
        for col in range(1, cols):
            if first[row - 1] == second[col - 1]:
                matrix[row][col] = matrix[row - 1][col - 1] + 1
            else:
                matrix[row][col] = max(matrix[row - 1][col], matrix[row][col - 1])

    result_representation(matrix, first, second)


if __name__ == "__main__":
    main()

"""
    Possible Inputs:

13 42 69 73 42 84 26
13 54 73 42 8 15 29

5 69 78 5 3 5 5 5
1 2 3 5 5 5 5 5

"""
