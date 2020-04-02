'''
“Given a base 10 number, print the 
hexidecimal (base  16) representation 
of that number.”

Notes: 
- to convert hex to decimal multiply the hex number by 16 

example: 
9 = 9 * (16 ^ 0) = 9
C = 12 * (16 ^ 1) = 192
results: 192 + 9 = 20110 decimal

pseudocode: 
given a hex string, loop through the elements of the string, 
convert the element value into number representations 

0-9 --> 0-9
A-F --> 10-15

then multiply each value by 16. Lastly, add up the
multiplied numbers together. 
'''

class Solution:
    def hexToDecimal(self, num: String):
        
