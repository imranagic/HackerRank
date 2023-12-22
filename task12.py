"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to

Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, string.
The second line contains the width, max_width .

Constraints
0 < len(string) < 1000
0 < max_width < len(string)
Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""



#import textwrap

def wrap(string, max_width):
    #return textwrap.fill(string,max_width) #One line code solution with built-in function
    newstring = ''
    br = 0
    for i in string:
        if br == max_width:
            newstring += '\n' + i
            br = 1
        else:
            newstring += i
            br = br + 1
    return newstring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    while len(string) < 1 or len(string) > 999:
        string = input()
    
    while len(max_width) < 1 or len(max_width) > len(string):
        max_width = int(input())
    
    print(result)