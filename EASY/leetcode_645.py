# 645. Set Mismatch

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
# due to some error, one of the numbers in s got duplicated to another number in the set, which results in
# repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.


Solution - 
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        
        # Change every number index with multiple of -1
        for n in nums:
            if nums[abs(n)-1] < 0:
                res[0] = abs(n)
            else:
                nums[abs(n)-1] *= -1
        # If number is > 0 means that element has not been changes in prev for loop
        # means that is missing number
        for i in range(len(nums)):
            if nums[i]>0:
                res[1] = i+1
        return res 