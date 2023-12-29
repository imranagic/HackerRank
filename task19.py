"""

Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Output Format

Print the space separated elements of deque d.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2

"""


from collections import deque
n = int(input())

d = deque()
for _ in range(n):
    opt = input().split()
    if hasattr(d, opt[0]):
        if len(opt)>1:
            getattr(d,opt[0])(opt[1])
        else:
            getattr(d,opt[0])()
    else:
        print("Wrong attribute")

    """
    operation = opt[0]
    if(operation == 'append'):
        d.append(opt[1])
    elif(operation == 'pop'):
        d.pop()
    elif(operation == 'popleft'):
        d.popleft()
    elif(operation == 'appendleft'):
        d.appendleft(opt[1])
    """
print(*d)


