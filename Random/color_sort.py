"""
You work at a sorting factory. You sort things. One day, your boss comes in to tell you there's a new ball shipment. There are three kinds of balls: red, white, and blue. You've been charged with the task of sorting these balls. Unfortunately, your boss won't let you take your lunch break until you've finished sorting the balls, so you want to do it quickly.

Instructions:
Create an algorithm that will sort an array of n elements, each element either red, white or blue. The integers 0, 1, 2, will represent red, white, and blue, respectively. Perform this sorting in-place, using constant space. Your solution should complete this in O(n) time, any longer and you'll miss your lunch break!

Example:
[0, 1, 0, 1, 2, 1] --> [0, 0, 1, 1, 2]

Extra Challenge:
The boss is threatening to replace your job with a very efficient sorting robot, provided you don't perform better than it would. Luckily for you, the robot requires taking two passes over the array to sort the elements. You're not sure, but you think there might be a way to sort the elements that requires taking only one pass over the array, thus handily out-performing the robot.

Original Platform:  https://leetcode.com/problems/sort-colors/

notes: 
- for every element in the list
  - if the element is a 0, prepend it to the front 
  - if element is 1, leave it alone 
  - if 2, append to the end of the list 
"""

def color_sort(nums):

  for index in range(len(nums)):
    # if the number at the current index is 0 
    if nums[index] == 0:
      # remove num from index and add to front of the list 
      nums.insert(0, nums.pop(index))
    # if number at current index is 2
    if nums[index] == 2: 
      # append to the end of the list 
      nums.append(nums.pop(index))
  return nums

  print(color_sort([0, 0, 2, 2, 1]))