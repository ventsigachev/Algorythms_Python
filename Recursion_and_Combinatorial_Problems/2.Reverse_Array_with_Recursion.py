def reversing(list_to_reverse, l_ind, ind=0):
    if ind == len(list_to_reverse) // 2:
        print(*list_to_reverse)
        return
    list_to_reverse[ind], list_to_reverse[l_ind - ind] = list_to_reverse[l_ind - ind], list_to_reverse[ind]
    reversing(list_to_reverse, l_ind, ind + 1)


def main():
    list_to_reverse = input().split()
    last_index = len(list_to_reverse) - 1
    reversing(list_to_reverse, last_index)


if __name__ == "__main__":
    main()
