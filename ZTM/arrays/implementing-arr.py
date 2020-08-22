"""
Look-up/Accses - O(1)
Push/Pop - O(1)*
Insert - O(n)
Delete - O(n)
"""

class array_implementation:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item 
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        for item in range(index, self.length-1):
            self.data[item] = self.data[item + 1] # shift elements 1 space to the left from current index
        del self.data[self.length - 1] # delete last item 
        self.length -= 1
        

new_array = array_implementation()
new_array.push(7)
new_array.push("hello")
new_array.push("!")
new_array.pop()
# new_array.delete(2)

print(new_array)
