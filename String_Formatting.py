'''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary

# Function Description

Complete the print_formatted function in the editor below.


# Sample Input

17

# Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

# Link to question - https://www.hackerrank.com/challenges/python-string-formatting/problem
'''

def print_formatted(number):
    # your code goes here
    # calculating the longest width to match output pattern
  
    w = len(f'{number:b}')
  
    for num in range(1, number+1):
        print(f'{num:{w}d} {num:{w}o} {num:{w}X} {num:{w}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


