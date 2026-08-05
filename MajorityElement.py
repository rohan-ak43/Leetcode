class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        for j in hashmap:
            if hashmap[j] > (n/2):
                return j