"""
You are given a space separated list of integers. If all the integers are positive, 
then you need to check if any integer is a palindromic integer.
Input Format
The first line contains an integer N. M is the total number of integers in the list.
The second line contains the space separated list of N integers.
Constraints
0 < N < 100
Output Format
Print True if all the conditions of the problem statement are satisfied. 
Otherwise, print False.
Sample Input
5
12 9 61 5 14
Sample Output
True
Explanation
Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.

"""

n = int(input())
myl = list(map(int,input().split()))

while n<0 or n>99:
    n = int(input())

print(all([num>0 for num in myl]) and any([str(num) == str(num)[::-1] for num in myl]))