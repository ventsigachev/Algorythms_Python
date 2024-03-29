"""
    We have two strings, s1 and s2. The goal is to obtain s2 from s1 by applying the following operations:
    • replace(i, x) – in s1, replaces the symbol at index  with the character x
    • insert(i, x) – in s1, inserts the character x at index i
    • delete(i) – from s1, removes the character at index i
    We are only allowed to modify s1, s2 always stays unchanged. Each of the three operations has a certain cost
    associated with it (positive integer number).
    Note: the cost of replace(i, x) operation is 0, if it does not change the character.
    The goal is to find the sequence of operations which will produce s2 from s1 with minimal cost.

    Input
        • The input consists of five lines.
        • The first line is replacement cost.
        • The second line is insert cost.
        • The third line is deleted cost.
        • After that on the next two lines are the two strings s1 and s2.
"""


def main():
    replacement_cost = int(input())
    insert_cost = int(input())
    delete_cost = int(input())

    f_str = input()
    s_str = input()

    r = len(f_str) + 1
    c = len(s_str) + 1

    matrix = []

    for _ in range(r):
        matrix.append([0] * c)

    for col in range(1, c):
        matrix[0][col] = matrix[0][col - 1] + insert_cost

    for row in range(1, r):
        matrix[row][0] = matrix[row - 1][0] + delete_cost

    for row in range(1, r):
        for col in range(1, c):
            if f_str[row - 1] == s_str[col - 1]:
                matrix[row][col] = matrix[row - 1][col - 1]
            else:
                matrix[row][col] = min(matrix[row][col - 1] + insert_cost, matrix[row - 1][col] + delete_cost,
                                       matrix[row - 1][col - 1] + replacement_cost)

    result = matrix[r - 1][c - 1]
    print(f"Minimal cost: {result}")


if __name__ == "__main__":
    main()

"""
    Possible Inputs:
    
3
2
1
abracadabra
mabragabra

3
3
3
equal
equal

1
1
1
equal
different

"""
