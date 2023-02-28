"""
    Efficient sorting algorithm. Choose a pivot; move smaller elements left & larger right; sort left & right.
    Memory: O(log(n)) -> stack space (recursion). Time: O(n2) -> when the pivot element divides the array into two
    unbalanced sub-arrays (huge difference in size). Stable: Depends. Method: Partitioning.
    Average Performance: O(log(n)). Divide and Conquer Algorithm.
"""


def quick_sort(arr, start, end):

    if start >= end:
        return

    pivot, left, right = start, start + 1, end

    while left <= right:
        if arr[left] > arr[pivot] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

    return arr


def main():

    nums = [int(x) for x in input().split()]
    start = 0
    end = len(nums) - 1
    print(*quick_sort(nums, start, end))


if __name__ == "__main__":
    main()


"""
    Possible Input:
    
    5 4 3 2 1
    
    13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43
    
"""
