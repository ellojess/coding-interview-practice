"""
Create a function that reverses a string: 
    'Hi my name is Jess' should be:
    --> 'sseJ si eman ym iH'

Input: string 
Output: string 

- check input is a string
- check that input is reversible (> 2 characters)

- loop through the given string
- join each character in the beginning to obtain the reversed string
"""

def reverse_string(str):

    if not str or len(str) < 2:
        return f"oops: cannot reverse \"{str}\""

    reversed_str = ""
    
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("Hi my name is Jess")) # should print: sseJ si eman ym iH
print(reverse_string("F")) # should print: oops: cannot reverse "O"
