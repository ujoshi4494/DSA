# 380. Insert Delete GetRandom O(1)
# Implement the RandomizedSet Class

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# Solution - 
class RandomizedSet:

    def __init__(self):
        # Use Dictionary to hold index position for values
        # Use Array to hold all values
        self.map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        # If element is present return False immediately
        # Otherwise put it in dictionary with value length of array
        if val in self.map:
            return False
        self.map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        # While remove element First find lastElement and its index
        # put lastElement at place of val index
        if val not in self.map:
            return False
        lastElement = self.nums[-1]
        valIndex = self.map[val]

        # Set lastElement at removed value index
        self.nums[valIndex] = lastElement
        self.map[lastElement] = valIndex

        # delete val from dictionary and array
        del self.map[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums)-1)]