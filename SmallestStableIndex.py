class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            currentm = max(nums[:i+1])
            currentmin = min(nums[i:])
            if currentm - currentmin <= k:
                return i
        return -1 