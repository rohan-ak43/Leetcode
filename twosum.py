# Solution 1 - Brute Force Method
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return i,j

# Solution 2 - Hashmap (Optimal solution)  
class Solution(object):
    def twoSum(self, nums, target):
        hashm = {}
        for i,num in enumerate(nums):
            com = target - num 
            if com in hashm:
                return [hashm[com],i]
            hashm[num] = i 