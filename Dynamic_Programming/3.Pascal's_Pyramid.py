"""
    Write a program that finds the binomial coefficient  for given non-negative integers n and k.

"""


def binomial_coefficient(n, k, cache=None):
    if cache is None:
        cache = {}

    key = f'{n}{k}'
    if key in cache:
        return cache[key]

    if n == 0 or k == 0 or n == k:
        return 1

    result = binomial_coefficient(n - 1, k - 1, cache) + binomial_coefficient(n - 1, k, cache)
    cache[key] = result

    return result


def main():
    n = int(input())
    k = int(input())

    print(binomial_coefficient(n, k))


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
