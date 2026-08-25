class Solution(object):
    def alternateDigitSum(self, n):
        new = str(n)
        result = 0
        for i in range(0,len(new),2):
            result += int(new[i])
        for j in range(1,len(new),2):
            result -= int(new[j])
        return result