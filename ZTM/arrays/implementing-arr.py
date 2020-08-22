"""
Look-up/Accses - O(1)
Push/Pop - O(1)*
Insert - O(n)
Delete - O(n)
"""

class array_implementation:
    def __init__(self):
        self.length=0
        self.data={}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item 
        self.length += 1
        return self.length


new_array = array_implementation()
print(new_array.push(3))

