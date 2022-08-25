'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 
'''

import random

class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        else:
            self.hash_map[val] = len(self.values)
            self.values.append(val)
        # print(self.values)  
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        else:
            idx = self.hash_map[val]
            
            self.hash_map[self.values[-1]], self.hash_map[val] = self.hash_map[val], self.hash_map[self.values[-1]] 
            
            self.values[idx], self.values[-1] = self.values[-1], val
            
            self.hash_map.pop(val)
            self.values.pop()
            
        # print(self.values)
        return True
    
    def getRandom(self) -> int:
        # print(self.values)
        # keys = list(self.hash_map.keys())
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
