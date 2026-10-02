# Solution 1
class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(31):
            if 2**i == n:
                return True
        return False

# Solution 2
class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(31):
            ans = 2 ** i
            if ans == n:
                return True
        return False