'''
Prompt: 
Given an array of integers, return indices of the two 
numbers such that they add up to a specific target.

You may assume that each input would have 
exactly one solution, and you may not use the same 
element twice.

Summary: 
Find the indices of two numbers that add up to a specific target.

Example: 
Input: [2,7,11,15, 3], Target: 10 
Output: [1,4]

- track the values and indeces of every item in a list
- store values as keys in a dictionary 
- loop through the array and see if the difference between that 
value and the target is a key within the dictionary, 
- continue until an array value and key add up to the target
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        