"""
Prompt: 
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

Variable Table:             0  1  2  3  4   length: 5
nums: [4,1,2,1,2], sorted: [1, 1, 2, 2, 4]
i: 1

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums = sorted(nums)
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        for i in range(2, len(nums)-1):
            if (nums[i] != nums[i-1]) and (nums[i] != nums[i+1]):
                return nums[i]