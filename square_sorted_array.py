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

# Solution 3
class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            sq = nums[i]**2
            nums[i] = sq
        nums.sort()
        return nums