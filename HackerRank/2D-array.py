#!/bin/python3

"""
Prompt: 
Given a 6x6 2D Array, arr: 

    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

We define an hourglass in  "A" to be a subset of values with 
indices falling in this pattern in arr's graphical representation:

    a b c
      d
    e f g

There are 16 hourglasses in arr, and an hourglass sum is the sum 
of an hourglass' values. Calculate the hourglass sum for every 
hourglass in arr, then print the maximum hourglass sum.

    For example, given the 2D array:

        -9 -9 -9  1 1 1 
        0 -9  0  4 3 2
        -9 -9 -9  1 2 3
        0  0  8  6 6 0
        0  0  0 -2 0 0
        0  0  1  2 4 0

 We calculate the following 16 hourglass values:

    -63, -34, -9, 12, 
    -10, 0, 28, 23, 
    -27, -11, -2, 10, 
    9, 17, 25, 18

Our highest hourglass value is 28 from the hourglass:

    0 4 3
      1
    8 6 6

Function Description: 

Complete the function hourglassSum in the editor below. 
It should return an integer, the maximum hourglass sum in the array.
hourglassSum has the following parameter(s):

    arr: an array of integers

Sample Input:

    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 2 4 4 0
    0 0 0 2 0 0
    0 0 1 2 4 0

Sample Output:

    19


Time Complexitity Analysis: 
Run time would be O(n^2)
Space Complexity Analysis: 
O(n^2) due to array being 2D array
""" 

import math
import os
import random
import re
import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

max_hourglass_sum = -9 * 7 

for row in range(len(arr) - 2):
    for column in range(len(arr[row]) - 2):
        tl = arr[row][column]
        tc = arr[row][column + 1]
        tr = arr[row][column + 2]
        mc = arr[row + 1][column + 1]
        bl = arr[row + 2][column]
        bc = arr[row + 2][column + 1]
        br = arr[row + 2][column + 2]
        current_hourglass_sum = tl + tc + tr + mc + bl + bc + br
        max_hourglass_sum = max(current_hourglass_sum, max_hourglass_sum)

print(max_hourglass_sum)
