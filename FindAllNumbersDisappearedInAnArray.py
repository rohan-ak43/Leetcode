#Soultion 1 - Brute Force Method
class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        new = []
        hasht = set()
        for i in nums:
            hasht.add(i)
        for j in range(1,len(nums)+1):
            if j not in hasht:
                new.append(j)
        return new