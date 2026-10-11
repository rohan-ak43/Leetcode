class Solution(object):
    def sumOfSquares(self, nums):
        length = len(nums)
        sums = 0
        for i in range(length):
            n = i + 1
            if length % n == 0:
                sums += nums[i] * nums[i]
        return sums 