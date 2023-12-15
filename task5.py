"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any students) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print
each name on a new line.
Example
records = [[" chi" , 20.0], ["beta", 50.0], [" alpha", 50.0]]
The ordered list of scores is [20.0, 50.0]. so the second lowest score is 50.0. 
There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:
alpha 
beta
Input Format
Leaderboard
The first line contains an integer. N, the number of students 
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.
Constraints
• 2 <= N <= 5
• There will always be one or more students having the second lowest grade.
Output Format
Print the name(s) of any students) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.

"""


if __name__ == '__main__':
    mylist = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        mylist.append([name,score])
        scores.append(score)
     
    sls = sorted(set(scores))[1]
    names = []
    for [name,score] in mylist:
       if score == sls:
           names.append(name)
   
    for name in sorted(names):
        print(name)

