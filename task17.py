"""

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  S= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string S.
Note: The string  will contain only uppercase letters: [A - Z].

"""

s='ANANAS'
vowels = ['A','E','I','O','U']
p1 = []
p2 = []

for i in range(0,len(s)):
    if s[i] not in vowels:
        #p1.append(s[0:len(s)-i])
        br = 0
        for j in range(i,len(s)):
            p1.append(s[i:len(s)-br])
            br += 1
    elif s[i] in vowels:
        br = 0
        for j in range(i,len(s)):
            p2.append(s[i:len(s)-br])
            br += 1
stuart = len(p1)
kevin = len(p2)
if(stuart > kevin):
    print(f"Stuart {len(p1)}")
elif(kevin > stuart):
    print(f"Kevin {len(p2)}")
else:
    print("Draw")

