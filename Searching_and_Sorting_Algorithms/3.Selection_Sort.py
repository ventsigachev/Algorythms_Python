"""
    Simple, but inefficient algorithm. Swap the first with the min element on the right, then
    the second, etc. Memory: O(1). Time: O(n2). Stable: No. Method: Selection.
"""


def selection_sort(nums):
    for min_ind in range(len(nums)):
        for curr_ind in range(min_ind + 1, len(nums)):
            if nums[min_ind] > nums[curr_ind]:
                nums[min_ind], nums[curr_ind] = nums[curr_ind], nums[min_ind]
    return nums


def main():
    nums_arr = [int(x) for x in input().split()]
    print(*selection_sort(nums_arr))


if __name__ == "__main__":
    main()


"""
Possible Inputs:

5 4 3 2 1


13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 
64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 
21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43

"""
