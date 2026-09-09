class Solution(object):
    def sumBase(self, n, k):
        sums = 0
        while n > 0:
            sums += n % k
            n //= k
        return sums 