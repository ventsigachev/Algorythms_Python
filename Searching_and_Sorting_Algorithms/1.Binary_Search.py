"""
 Binary search is applicable only on sorted lists.That is why instead of using linear search,
 with linear time(O(n)), we use binary search, with logarithmic time(O(log(n)).
 In this case with iterative search, to find the index, where the searched n is.
"""


def iterative_search(nums, start, end, n):
    while True:
        if start > end:
            break
        mid = (start + end) // 2

        if nums[mid] > n:
            end = mid - 1
        elif nums[mid] < n:
            start = mid + 1
        else:
            return mid
    return f"The searched number is not in the list"


def main():
    nums = [int(x) for x in input().split()]
    n = int(input())

    print(iterative_search(nums, 0, len(nums) - 1, n))


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