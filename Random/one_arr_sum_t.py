'''
Given an array a of n numbers and a target value t, find two numbers whose sum is t.
Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]
'''

# brute force solution 
def two_sum_with_nested_for(list_nums, target):
    # loop through arr twice
    for i in range(list_nums):
      for j in range(i+1, list_nums):
          # see if addends equal the target 
          if list_nums[i] + list_nums[j] == target:
              # if they do then return indices 
              return [i, j]

# alternative solution using map/dictionary 
def two_sum_with_map(list_nums, target):
    constants = {} # holds 

    for i in range(list_nums):
        # if present difference in numbers exist in dict 
        if target - list_nums[i] in constants:
            # then return as indices 
            return [constants[target - list_nums[i]], i]
        else: 
            # else put number into dict 
            constants[list_nums[i]] = i 