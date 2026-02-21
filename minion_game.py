'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

Sample Input

BANANA

Sample Output

Stuart 12

Note :
Vowels are only defined as `AEIOU`. In this problem,  is not considered a vowel.

Full link - https://www.hackerrank.com/challenges/the-minion-game/problem
'''
def minion_game(string):
    length = len(string)
    kevin, stuart = 0,0
    vowels = 'AEIOU'
    
    for i in range(0, length):
        if string[i] in vowels:
            kevin += (length - i)
        else:
            stuart += (length - i)
    
    if (stuart > kevin):
        print(f'Stuart {stuart}')
    elif (stuart == kevin):
        print('Draw')
    else:
        print(f'Kevin {kevin}')                    

if __name__ == '__main__':
    s = input()
    minion_game(s)

