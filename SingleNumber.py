# Soultion 1 - Using hashmap
class Solution(object):
    def singleNumber(self, nums):
        hashs = {}
        for i in nums:
            hashs[i] = hashs.get(i,0) + 1
        for key, item in hashs.items():
            if item == 1:
                return key