class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        small = nums[0]
        big = nums[-1]
        while big:
            small, big = big, small % big
        return small