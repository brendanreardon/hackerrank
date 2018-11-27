"""
Objective
Today, we're learning and practicing an algorithmic concept called Recursion.

Task
Write a factorial function that takes a positive integer,  as a parameter and prints the result of N! (N factorial).
"""

if __name__ == '__main__':
    def factorial(n):
        if n > 1:
            return n * factorial(n - 1)
        else:
            return 1

    N = int(input())
    result = factorial(N)
    print(result)

