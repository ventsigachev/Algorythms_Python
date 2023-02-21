def array_sum(nums, index=0):
    while index <= len(nums) - 2:
        return nums[index] + array_sum(nums, index + 1)
    return nums[index]


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(array_sum(arr))
