'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.

Print the capitalized string, .

# Sample Input

chris alan

# Sample Output

Chris Alan

Link to question : https://www.hackerrank.com/challenges/capitalize/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
# Capitalize() capitalize only first letter of the word: Eg - "this is string" to "This is string", so we need to split and capitalize every word first letter
# Title() capitalize every first letter of the sentence. Eg: "this is string" to "This Is String", but "They're" to "They'Re"
def solve(s):
    for char in s.split():
        s = s.replace(char,char.capitalize()) 
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

