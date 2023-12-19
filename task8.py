"""
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of 
the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
Example
N = 4
append 1
append 2
insert 3 1
print
Discussi
  append 1: Append 1 to the list, arr = [1].
• append 2: Append 2 to the list, arr = [1, 2].
• insert 3 1: Insert 1 at index 3, arr = [1, 2, 1].
• print: Print the array.
Output:
[1,2,1]
"""

if __name__ == '__main__':
    N = int(input())
    myl = []
    for _ in range(N):
        command = input().split()
        if command[0].lower() == 'insert':
            myl.insert(int(command[1]), int(command[2]))
        if command[0].lower() == 'print':
            print(myl)
        if command[0].lower() == 'remove':
            myl.remove(int(command[1]))
        if command[0].lower() == 'append':
            myl.append(int(command[1]))
        if command[0].lower() == 'sort':
            myl.sort()
        if command[0].lower() == 'pop':
            myl.pop()
        if command[0].lower() == 'reverse':
            myl = myl[::-1]
        