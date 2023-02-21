def gen_array(arr, index=0):
    if index == len(arr):
        print(*arr, sep='')
        return

    for n in range(2):
        arr[index] = n
        gen_array(arr, index + 1)


if __name__ == "__main__":
    num = int(input())
    list_ = [None] * num
    gen_array(list_)
