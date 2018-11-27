"""
Objective
Today, we're working with binary numbers.

Task
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
"""

# Apply the modulo operator to find if the remainder is zero or one
# If one, increase sequential ones by one and see if it exceeds the current best count
# Calculate the quotient and repeat until n != 0

if __name__ == '__main__':
    n = int(input())

    def modulo(a, b):
        return a % b

    def floor_division(a, b):
        return a // b

    sequential_ones = 0
    max_sequential_ones = 0

    while n != 0:
        remainder = modulo(n, 2)
        if remainder == 1:
            sequential_ones += 1
            max_sequential_ones = max(sequential_ones, max_sequential_ones)
        else:
            sequential_ones = 0

        quotient = floor_division(n, 2)
        n = quotient

    print(max_sequential_ones)