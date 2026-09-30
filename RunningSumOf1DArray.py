class Solution(object):
    def runningSum(self, nums):
        ans = [0] * len(nums)
        length = len(nums)
        for i in range(length):
            for j in range(i+1):
                ans[i] += nums[j]
        return ans