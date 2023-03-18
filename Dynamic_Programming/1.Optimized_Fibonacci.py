"""
    Dynamic programming solution for finding n-th Fibonacci member:
        • F0 = 0
        • F1 = 1
        ▪ Fn = Fn-1 + Fn-2
        ▪ Memoization → save/cache sub-problem solutions for later use
        ▪ Typically using an array, matrix or a hash table
    Recursive Fibonacci has ~ O(1.6n) complexity.
    Recursive Fibonacci (with memorization) has ~ O(n) complexity.
    If we want to find the 36-th Fibonacci number:
        ▪ Recursive solution takes 48 315 633 steps
        ▪ Iterative or recursive (with memorization) takes ~36 steps
"""
import time


def calculate_fibonacci(n, hashing):
    if n in hashing:
        return hashing[n]

    if n == 0:
        return 0

    if n <= 2:
        return 1

    result = calculate_fibonacci(n - 1, hashing) + calculate_fibonacci(n - 2, hashing)
    hashing[n] = result

    return result


def main():
    n_th_fibonacci_member = int(input())
    hash_table = {}

    start = time.time()
    print(calculate_fibonacci(n_th_fibonacci_member, hash_table))
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:
20  ---->   6765

50  ---->   12586269025

36  ---->   14930352,   time: with hashing - 0.00012612342834472656 sec., without hashing - 5.2672953605651855 sec.

"""
