class Solution(object):
    def removeDuplicates(self, nums):
        unique = []
        check = list(nums)
        for i in range(len(nums)):
            if nums[i] in check:
                unique.append(nums[i])
        for j in unique:
            if j in nums:
                if nums.count(j)>1:
                    nums.remove(j) 
        k = len(unique)
        return k    