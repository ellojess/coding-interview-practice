class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size # initialize array of size 'size'

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        hash = 0 
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

food_hash_table = HashTable(2)
print(food_hash_table.hash('4'))