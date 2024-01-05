"""

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in setB . 
Your initial happiness is 0. For each i integer in the array, if i in A, 
you add 1 to your happiness. If i in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format

The first line contains integers n and , separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1

"""
n,m = [int (x) for x in input().split()]

l = list(map(int, input().split()))

a = set(map(int, input().split()))

b = set(map(int, input().split()))

hap = 0

for i in l:
    if i in a:
        hap += 1
    elif i in b:
        hap -= 1
print(hap)

#print(sum([(i in a) - (i in b) for i in l])) #one line solution
