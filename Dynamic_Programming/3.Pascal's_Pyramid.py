"""
    Write a program that finds the binomial coefficient  for given non-negative integers n and k.

"""


def binomial_coefficient(n, k):
    if n == 0 or k == 0 or n == k:
        return 1


def main():
    n = int(input())
    k = int(input())

    binomial_coefficient(n, k)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
    
3
2

4
0

6
2

49
10

"""
