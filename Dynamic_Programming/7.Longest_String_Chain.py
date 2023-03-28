"""
    Given a list of strings, write a program that returns the longest string chain that can be built from those strings.
    A string chain is defined as follows: subsequence of a given sequence in which the subsequence's elements
    are in sorted order (string length), lowest to highest, and in which the subsequence is as long as possible.
    If several sequences with equal length exist, find the left-most of them.
"""


def main():
    sequence = input().split()
    size = [0] * len(sequence)
    previous = [None] * len(sequence)
    best_size = 0
    best_ind = 0

    for i in range(len(sequence)):
        word = sequence[i]
        c_size = 1
        parent = None

        for p_i in range(i - 1, -1, -1):
            p_word = sequence[p_i]

            if len(p_word) >= len(word):
                continue

            if size[p_i] + 1 >= c_size:
                c_size = size[p_i] + 1
                parent = p_i

        size[i] = c_size
        previous[i] = parent

        if c_size > best_size:
            best_size = c_size
            best_ind = i

    print(best_ind)
    print(best_size)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:

a ab abcd abc

a ab abcd abc abcd abcde

abde abc abd abcde ade ae 1abde abcdef

"""
