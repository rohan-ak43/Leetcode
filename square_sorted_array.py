# Solution 1
class Solution(object):
    def sortedSquares(self, nums):
        square = [i * i for i in nums]
        square.sort()
        return square


# Solution 2
class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums