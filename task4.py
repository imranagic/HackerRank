"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains an array [I of n integers each separated by a space.
Constraints
• 2 < n ≤ 10
• - 100 < A[i] ≤ 100
Output Format
Print the runner-up score
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    br=-1
    secMax = arr[br-1]
    while arr[br-1] == arr[-1] :
        br -= 1
        secMax = arr[br-1]
    print(secMax)