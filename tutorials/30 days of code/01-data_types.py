'''
Objective
Today, we're discussing data types. Check out the Tutorial tab for learning materials and an instructional video!

Task
Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:

1. Declare  variables: one of type int, one of type double, and one of type String.
2. Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
3. Use the  operator to perform the following operations:
    1. Print the sum of  plus your int variable on a new line.
    2. Print the sum of  plus your double variable to a scale of one decimal place on a new line.
    3. Concatenate  with the string you read as input and print the result on a new line.
'''

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
integer = int(4)
double = float(4.0)
string = str('Hello')

# Read and save an integer, double, and String to your variables.
input_integer = int(input())
input_float = float(input())
input_str = str(input())

# Print the sum of both integer variables on a new line.
summed_i = i + input_integer
print(summed_i)

# Print the sum of the double variables on a new line.
summed_d = d + input_float
print(summed_d)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print('{}{}'.format(s, input_str))
