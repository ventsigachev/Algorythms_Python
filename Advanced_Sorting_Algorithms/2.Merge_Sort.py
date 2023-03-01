"""
    Efficient sorting algorithm. Divide and Conquer Algorithm.
    Divide the list into sub-lists (typically 2 sub-lists)
        1. Sort each sub-list (recursively call merge-sort)
        2. Merge the sorted sub-lists into a single list
    Memory: O(n) / O(n*log(n))
    Time: O(n*log(n)). Highly parallelize on multiple cores / machines → up to O(log(n)).
"""


def merge_arrays(left, right):
    sorted_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_arr.append(left[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        sorted_arr.append(left[left_idx])
        left_idx += 1
    while right_idx < len(right):
        sorted_arr.append(right[right_idx])
        right_idx += 1

    return sorted_arr


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_ind = len(nums) // 2
    left = nums[: mid_ind]
    right = nums[mid_ind:]

    return merge_arrays(merge_sort(left), merge_sort(right))


def main():
    nums = list(map(int, input().split()))
    print(*merge_sort(nums))


if __name__ == "__main__":
    main()


"""
Possible Inputs:

5 4 3 2 1

13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43

"""
