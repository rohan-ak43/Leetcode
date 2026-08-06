class Solution(object):
    def thirdMax(self, nums):
        nums2 = list(set(nums))
        result = sorted(nums2,reverse = True)
        if len(result) < 3:
            return result[0]
        else:
            return result[2]