def rec_drawing(num):
    if num == 0:
        return
    print("*" * num)
    rec_drawing(num - 1)
    print("#" * num)


if __name__ == "__main__":
    number = int(input())
    rec_drawing(number)
