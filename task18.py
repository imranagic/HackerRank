"""

You are given  words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
1 <= n <= 10^5
The sum of the lengths of all the words do not exceed 10^6
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, n.
The next n lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

"""

n = int(input())

words = [input() for i in range(n)]

words = list(map(lambda word: word.lower(), words))

num = len(set(words))

words_dic = {}

for word in words:
    if word in words_dic:
        words_dic[word] += 1
    else:
        words_dic[word] = 1
    
print (num)

for item in words_dic:
    print(words_dic[item], end=" ")



