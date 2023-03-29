"""
    A zigzag sequence is one that alternately increases and decreases. More formally, such a sequence has to comply
    with one of the two rules below:
    1) Every even element is smaller than its neighbors and every odd element is larger than its neighbors, or
    2) Every odd element is smaller than its neighbors and every even element is larger than its neighbors
    1 3 2 is a zigzag sequence, but 1 2 3 is not. Any sequence of one or two elements is zigzag.
    Find the longest zigzag subsequence in a given sequence.
"""


def main():
    nums = [int(x) for x in input().split()]
    matrix = []
    [matrix.append([0] * len(nums)) for _ in range(2)]
    matrix[0][0] = matrix[1][0] = 1
    result_size = 0
    last_ind = 0

    for current in range(1, len(nums)):
        current_num = nums[current]
        for prev in range(current - 1, -1, -1):
            prev_num = nums[prev]

            if current_num > prev_num and matrix[1][prev] + 1 >= matrix[0][current]:
                matrix[0][current] = matrix[1][prev] + 1

            if current_num < prev_num and matrix[0][prev] + 1 >= matrix[1][current]:
                matrix[1][current] = matrix[0][prev] + 1

        if matrix[0][current] > result_size:
            result_size = matrix[0][current]
            last_ind = current
        if matrix[1][current] > result_size:
            result_size = matrix[1][current]
            last_ind = current

    print(result_size)
    print(last_ind)
    

if __name__ == "__main__":
    main()

"""
    Possible Inputs:

8 3 5 7 0 8 9 10 20 20 20 12 19 11

1 2 3

1 3 2

24 5 31 3 3 342 51 114 52 55 56 58

"""
