class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size # initialize array of size 'size'

    def __str__(self):
       return str(self.__dict__)

    def _hash(self, key):
        """Return hash table"""
        hash = 0 
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size # ord(key[i]) gives unicode code point of character key[i]
        return hash

    def set(self, key, value):
        address = self._hash(key)

        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        hash_value = self._hash(key)
        reference = self.data[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return None

    def keys(self): 
        keys_arr = [] 
        for i in range(self.size):
            if self.data[i] != None:
                for j in range(len(self.data[i])):
                    keys_arr.append(self.data[i][j][0])
        return keys_arr
        

food_hash_table = HashTable(2)
food_hash_table._hash('4')
food_hash_table.set("grapes", 300)
food_hash_table.set("appless", 123)
print(food_hash_table.get("grapes"))

print(food_hash_table)