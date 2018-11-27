"""
Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
"""

if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        string = str(input())
        string_list = list(string)
        evens = []
        odds = []
        for index, letter in enumerate(string_list):
            if index % 2 == 0:
                evens.append(letter)
            else:
                odds.append(letter)
        string_evens = ''.join(evens)
        string_odds = ''.join(odds)
        print('{} {}'.format(string_evens, string_odds))
