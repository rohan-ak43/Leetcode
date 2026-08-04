class Solution(object):
    def findErrorNums(self, nums):
        hashm = {}
        duplicate = None
        missing = None
        for i in nums:
            hashm[i] = hashm.get(i,0)+1
        for i in range(1,len(nums)+1):
            if i not in hashm:
                missing = i
            elif hashm[i]>1:
                duplicate = i
        return [duplicate,missing]