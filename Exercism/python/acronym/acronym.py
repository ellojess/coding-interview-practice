"""
- get the first letter of every word and capitalize it 
- append each letter to a string and return the string 

- handle spaces, - , _ , and other punctuations 

"""

def abbreviate(words):
  acronym = ""
  wrds = words.replace('-', ' ').replace('_',' ').split() 
  for word in wrds:
    acronym += word[0].upper()

  return acronym
