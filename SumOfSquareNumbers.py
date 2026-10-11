class Solution(object):
    def judgeSquareSum(self, c):
        sqr = int(sqrt(c))
        for a in range(sqr + 1):
            b = sqrt(c - (a*a))
            if b == int(b):
                return True
        return False