class Solution(object):
    def missingNumber(self, nums):
        hasht = set()
        nums.sort()
        for i in nums:
            hasht.add(i)
        mini = 0
        maxi = nums[-1]
        for i in range(mini, len(nums) + 1):
            if i not in hasht:
                return i