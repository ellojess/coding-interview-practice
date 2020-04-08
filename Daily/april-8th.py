"""Given a list of n numbers, determine if it contains any duplicate numbers.
Jessica Trinh

Find duplicates in an array of numbers 

Numbers are whole 
Account for negatives
Assume that the list of numbers is unsorted 
Return Bool for whether or not a duplicate exists 
And number that appears 2+ is a duplicate 

Example: 

[-3, 5, 6, -7, 8, 9, 10, 11, 5, 10, 2, -6] → True 

Walkthrough: 

Option A: 
Sort the array
As we’re looping through, if the value already exists in the set, return True 

Option B: 
Loop through the indexes and append each value to a set if the value doesn’t already exist in the set 
Compare the sorted list to the set 
Equal in length first 
See if the values of list are equal
If they are, then return true 
If not then False """

list: [int] = [-3, 5, 6, -7, 8, 9, 10, 11, 5, 10, 2, -6]

# def checkDuplicates(list): 
# 	sortedList = list.sort() 
# 	setList = set() 
# 	for item in sortedList: 
# 		setList.append(item)
# 		if item in setList:
# 			return True
# 		else: 
# 			return False 

# checkDuplicates(list)

def checkDuplicates(list): 
	setList = set() 
	for item in list: 
		setList.add(item)
		if item in setList:
		    return True
		else: 
		    return False

print(checkDuplicates(list))
		
# ** What’s the benefit of sorting when looking for duplicates? 
