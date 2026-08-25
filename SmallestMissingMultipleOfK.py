class Solution(object):
    def missingMultiple(self, nums, k):
        hasht = set(nums)
        curr = k
        while curr in hasht:
            curr += k
        return curr