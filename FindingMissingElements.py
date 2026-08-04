#Solution 1 - Hashset
class Solution(object):
    def findMissingElements(self, nums):
        new = []
        hasht = set()
        nums.sort()
        mini = nums[0]
        maxi = nums[-1]
        for i in nums:
            hasht.add(i)
        for j in range(mini, maxi + 1):
            if j not in hasht:
                new.append(j)
        return new

#Solution 2 - Brute Force
class Solution(object):
    def findMissingElements(self, nums):
        new = []
        nums.sort()
        mini = nums[0]
        maxi = nums[-1]
        for i in range(mini, maxi + 1):
            if i not in nums:
                new.append(i)
        return new