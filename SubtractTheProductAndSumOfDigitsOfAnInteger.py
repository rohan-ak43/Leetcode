class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        sums = 0
        for i in str(n):
            prod *= int(i)
            sums += int(i)
        result = prod - sums
        return result