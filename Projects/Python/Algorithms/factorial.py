# Brennon York  |  Math Algorithms  |  9/19/2026

from functools import lru_cache


def factorial(n):
    if n > -1:
        if n == 1 or n == 0:
            return 1
        else:
            ans = n * (factorial(n-1))
            return ans
    else:
        return "Factorial of negatives is not possible."


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(int(input("N = ?: "))))
print(factorial(int(input("N = ?: "))))
