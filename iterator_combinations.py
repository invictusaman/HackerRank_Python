'''
itertools.combinations(iterable, r)

This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

input_val = input().split()
string = input_val[0]
max_len = int(input_val[1])

sorted_string = sorted(string)

# Print single letters
for char in sorted_string:
    print(char)

# Print all combinations from length 2 to max_len
for r in range(2, max_len + 1):
    for pair in combinations(sorted_string, r):
        print(''.join(pair))
