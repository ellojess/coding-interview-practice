'''
Given a sorted array nums, remove the duplicates in-place such that each 
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

Example: 
Given nums = [1,1,2],
Your function should return length = 2, with the first two 
elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means 
modification to the input array will be known to the caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

Pseudocode:
- loop through array with two-pointer
- one, that would keep track of the current element in the 
original array and another one for just the unique elements.
- if duplicate appears, bypass it until unique number is seen 
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        
        for i in range(1, len(nums)):
            if nums[current] != nums[i]:
                current += 1
                nums[current] = nums[i]
        return current + 1