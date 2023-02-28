"""
    Simple, but inefficient algorithm. Move the first unsorted element left to its place.
    Memory: O(1). Time: O(n2). Stable: Yes. Method: Insertion.
    The optimization here is added break statement in inner for loop, when if statement is False,
    which means that all nums left to the current index are sorted.
"""


def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums


def main():
    nums = list(map(int, input().split()))
    print(*insertion_sort(nums))


if __name__ == "__main__":
    main()


"""
Possible Inputs:

5 4 3 2 1

13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43

"""
