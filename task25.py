"""

You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set([1,3,4]) is a strict superset of set([1,3]).
Set([1,3,4]) is not a strict superset of set ([1,3,4]).
Set ([1,3,4]) is not a strict superset of set ([1,3,5]).

Input Format

The first line contains the space separated elements of set A.
The second line contains integer , the number of other sets.
The next  lines contains the space separated elements of the other sets.

Constraints
0 < len(set(A)) < 501
0 < n < 21
0 < len(otherSets) < 101

Output Format

Print True if set  is a strict superset of all other  sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0

False

"""

s = set(map(int, input().split()))

n = int(input())

se = [set(map(int, input().split())) for i in range(n)]

c = 0
for i in range(len(se)):
    if(se[i].issubset(s) and len(s)>len(se[i])):
        c+=1

if(c == n):
    print("True")
else:
    print("False")
