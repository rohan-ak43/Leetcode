class Solution(object):
    def checkDivisibility(self, n):
        sum = 0
        prod = 1
        for i in str(n):
            sum += int(i)
            prod *= int(i)
        if n%(sum + prod) == 0:
            return True
        else:
            return False