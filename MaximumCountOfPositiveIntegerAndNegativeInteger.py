class Solution(object):
    def maximumCount(self, nums):
        negcount = 0
        poscount = 0
        for i in nums:
            if i == 0:
                continue
            elif i<0:
                negcount += 1
            else:
                poscount += 1
        if negcount < poscount:
            return poscount
        else:
            return negcount