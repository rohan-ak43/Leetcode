# Soultion 1 - Using hashmap
class Solution(object):
    def singleNumber(self, nums):
        hashs = {}
        for i in nums:
            hashs[i] = hashs.get(i,0) + 1
        for key, item in hashs.items():
            if item == 1:
                return key

# Solution 2 - Using XOR
class Solution(object):
    def singleNumber(self, nums):
        single = 0
        for i in nums:
            single ^= i
        return single