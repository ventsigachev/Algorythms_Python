def rec_factorial(num):
    while num > 0:
        return num * rec_factorial(num - 1)
    return 1


if __name__ == "__main__":
    number = int(input())
    print(rec_factorial(number))
