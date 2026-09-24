class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            sums = 0
            curr = nums[i]
            while curr > 0:
                sums += curr % 10
                curr //= 10
            if sums == i:
                return i
        return -1