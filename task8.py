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
        commands = input().split()
        command_name = commands[0].lower()
        if command_name == 'insert':
            myl.insert(int(command[1]), int(command[2]))
        elif command_name == 'print':
            print(myl)
        elif command_name == 'remove':
            myl.remove(int(command[1]))
        elif command_name == 'append':
            myl.append(int(command[1]))
        elif command_name == 'sort':
            myl.sort()
        elif command_name == 'pop':
            myl.pop()
        elif command_name == 'reverse':
            myl = myl[::-1]
        
