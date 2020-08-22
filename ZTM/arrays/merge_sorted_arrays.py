"""
Given two arrays that are sorted, merge the two arrays into a single sorted array 

parameters: 2 sorted arrays 
input: 2 arrays 
output: 1 array 

example: 
input: [0,3,4,31], [3,4,6,30]
output: [0, 3, 3, 4, 4, 6, 30, 31]

check conditions: 
- if there are two inputs
- if one of the inputs is an empty array 
- if both inputs are empty arrays 
- arrays are different lengths 
"""

def merge_sorted_arrays(arr1, arr2):
    merged_arr = []
    arr1_item = arr1[0]
    arr2_item = arr2[0]
    i = 1
    j = 1

    # check inputs 
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    if len(arr1) == 0 and len(arr2) == 0:
        return "both arrays are empty"

    while arr1_item or arr2_item:
        if arr1_item < arr2_item:
            merged_arr.append(arr1_item)
            arr1_item = arr1[i]
            i += 1
        else: 
            merged_arr.append(arr2_item)
            arr2_item = arr1[j]
            j += 1

    return merged_arr

print(merge_sorted_arrays([0,3,4,31], [3,4,6,30]))
print(merge_sorted_arrays([], [3,4,6,30]))
print(merge_sorted_arrays([0,3,4,31], [3,4]))