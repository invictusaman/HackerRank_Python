'''
You are given a string .
Your task is to find out whether  is a valid regex or not.

Input Format

The first line contains integer , the number of test cases.
The next  lines contains the string .

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
'''
# In python v3.11 and above, 

import re

n = int(input())

# pattern to detect possessive quantifiers
possessive_pattern = re.compile(r'(\*|\+|\?|\{\d+(,\d*)?\})\+')

for _ in range(n):
    reg = input()
    try:
        # Reject possessive quantifiers manually
        if possessive_pattern.search(reg):
            raise re.error("multiple repeat")

        re.compile(reg)
        print(True)
    except re.error:
        print(False)

# For older version <3.9

import re 

n = int(input()) 

for _ in range(n): 
  reg = input() 
  try: 
    re.compile(reg) 
    print(True) 
  except re.error: 
    print(False)
