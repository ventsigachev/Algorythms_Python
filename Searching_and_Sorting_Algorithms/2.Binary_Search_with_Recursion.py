"""
 Binary search is applicable only on sorted lists.That is why instead of using linear search,
 with linear time(O(n)), we use binary search, with logarithmic time(O(log(n)).
 In this case with recursive binary search, to find the index, where the searched n is.
"""


def recursive_search(nums, t, start, end):
    if start > end:
        return f"The searched number {t} is not in the list"

    mid = (start + end) // 2

    if nums[mid] > t:
        return recursive_search(nums, t, start, mid - 1)
    elif nums[mid] < t:
        return recursive_search(nums, t, mid + 1, end)
    elif nums[mid] == t:
        return f"The searched number {t} is on {mid} index in array"


def main():
    numbers = list(map(int, input().split()))
    tar = int(input())

    print(recursive_search(numbers, tar, 0, len(numbers) - 1))


if __name__ == "__main__":
    main()


""""
Possible Inputs:

1 2 3 4 5
1

-1 0 1 2 4
1

5 10 15 20 25 30
12
"""
