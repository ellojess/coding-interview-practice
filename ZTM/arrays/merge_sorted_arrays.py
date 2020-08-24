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

Steps: 
- compare first items from each array, append smallest to new array 

"""

def merge_sorted_arrays(arr1, arr2):
    merged_arr = []
    i, j = 0, 0

    # check inputs 
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1   
        else: 
            merged_arr.append(arr2[j])
            j += 1

    return merged_arr+arr1[i:]+arr2[j:]

print(merge_sorted_arrays([0,3,4,31], [3,4,6,30]))
print(merge_sorted_arrays([], [3,4,6,30]))
print(merge_sorted_arrays([0,3,4,31], [3,4]))
print(merge_sorted_arrays([],[]))