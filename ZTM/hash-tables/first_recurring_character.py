"""
Google Question
Given an array = [2,5,1,2,3,5,1,2,4]:
It should return 2

Given an array = [2,1,1,2,3,5,1,2,4]:
It should return 1

Given an array = [2,3,4,5]:
It should return undefined

- dict to store each element of array 
- iterate through array, see if item is already in dict
    - if yes, return element & break
    - else add item to dict & continue 

"""

def find_first_recurring(arr):
    char_dict = dict() 
    for item in arr:
        if item in char_dict:
            return item
        else:
            char_dict[item] = True
    return None

arr = [2,5,1,2,3,5,1,2,4]
print(find_first_recurring(arr))