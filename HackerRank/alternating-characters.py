"""
Prompt: 

Your task is to find the minimum number of required deletions.

Function Description

Complete the alternatingCharacters function in 
the editor below. It must return an integer representing 
the minimum number of deletions to make the alternating string.

alternatingCharacters has the following parameter(s):

s: a string

Sample Input
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output
3
4
0
0
4

Explanation
The characters marked red are the ones that can 
be deleted so that the string doesn't have matching 
consecutive characters.

Time analysis: O(n^2) due to the nested for loop 
Space analysis: O(n^2)

"""

n = int(input())
for _ in range(n):
    count = 0;
    word = input()
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    print(count) 