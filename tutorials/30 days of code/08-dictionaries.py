"""
Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.
"""

if __name__ == '__main__':
    n = int(input())
    split_input = [input().split(' ') for i in range(n)]
    phonebook = {name: number for name, number in split_input}
    while True:
        try:
            name = input()
            if name in phonebook:
                print('{}={}'.format(name, phonebook[name]))
            else:
                print('Not found')
        except:
            break
