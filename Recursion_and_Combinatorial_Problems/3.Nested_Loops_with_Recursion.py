def generate(arr, index=0):
    if index == len(arr):
        print(*arr)
        return

    for num in range(1, len(arr) + 1):
        arr[index] = num
        generate(arr, index + 1)


def main():
    n = int(input())
    list_ = [None] * n
    generate(list_)


if __name__ == "__main__":
    main()
