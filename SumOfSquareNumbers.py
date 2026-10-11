# Solution 1 
class Solution(object):
    def judgeSquareSum(self, c):
        sqr = int(sqrt(c))
        for a in range(sqr + 1):
            b = sqrt(c - (a*a))
            if b == int(b):
                return True
        return False

# Solution 2
class Solution(object):
    def judgeSquareSum(self, c):
        sqr = int(c**(0.5))
        for a in range(sqr + 1):
            b = (c - (a*a)) ** 0.5
            if b == int(b):
                return True
        return False