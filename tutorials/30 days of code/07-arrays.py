'''
Objective
Today, we're learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.
'''

if __name__ == '__main__':
    n = int(input())

    array = list(map(int, input().rstrip().split()))
    reversed_array = []
    for idx in range(n - 1, 0 - 1, -1):
        reversed_array.append(array[idx])
    reversed_array = ' '.join(map(str, reversed_array))
    print(reversed_array)
