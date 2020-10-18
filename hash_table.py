# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    
    def __init__(self, size=10):
        self.size = size
        self.data = []
        self.keyList = []
        self.valueList = []
        for i in range(0, size):
            self.data.append([])

    def __setitem__(self, key, newvalue):
        hashVal = self.hash(key)
        self.valueList.append(newvalue)
        if len(self.data[hashVal]) > 0: #Tests for existing key
            for x in self.data[hashVal]:
                if x[0] == key:
                    x[1] = newvalue #Puts new value into existing key array
                    return
        self.data[self.hash(key)].append([key, newvalue]) #only executes for novel keys
        self.keyList.append(key)
    
    def __getitem__(self, key):
        try:
            if self.data[self.hash(key)] == []:
                return None
            
            return self.data[self.hash(key)][0][1]
        except IndexError:
            return None
    
    def hash(self, key):
        return hash(key) % self.size

    def delete(self, key):
        hashVal = self.hash(key)
        if len(self.data[hashVal]) > 0:
            for x in self.data[hashVal]:
                if x[0] == key:
                    print("deleting val")
                    self.data[hashVal].remove(x)
                    return

    def clear(self):
        self.data = []
        for i in range(0, self.size):
            self.data.append([])

    def keys(self):
        return self.keyList

    def values(self):
        return self.valueList