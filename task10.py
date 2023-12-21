"""
You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string $ in the following manner:
• All sorted lowercase letters are ahead of uppercase letters
• All sorted uppercase letters are ahead of digits.
• All sorted odd digits are ahead of sorted even digits.
Input Format
A single line of input contains the string S.
Constraints
• 0 < len(S) < 1000
Output Format
Output the sorted string S.
Sample Input
Sorting1234
Sample Output
ginortS1324

"""
#Solution with list comprehension
word = input()
while(len(word) < 0 or len(word)>1000):
    word = input()
low = [char for char in word if char.islower()]
upp = [char for char in word if char.isupper()]
numsO = [char for char in word if char.isdecimal() and int(char) % 2 == 1]
numsE = [char for char in word if char.isdecimal() and int(char) % 2 == 0]

word = sorted(low) + sorted(upp) + sorted(numsO) + sorted(numsE)
print(*word) #This idea of unpacking is not mine but i liked it and put it 


"""
#Solution with for loop
word = input()
low = []
upp = []
numsO = []
numsE = []

for char in word:
    if char.islower():
        low.append(char)
    elif char.isupper():
        upp.append(char)
    elif char.isdecimal():
        if int(char)%2!=0:
            numsO.append(char)
        else:
            numsE.append(char)
word =  ''.join(sorted(low)) + ''.join(sorted(upp)) + ''.join(sorted(numsO)) + ''.join(sorted(numsE))
print(word)

"""