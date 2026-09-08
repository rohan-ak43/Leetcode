# Solution 1
class Solution(object):
    def countCommas(self, n):
        count = 0
        for i in range(1,n+1):
            if i >= 1000:
                count += 1
        return count

# Solution 2
class Solution(object):
    def countCommas(self, n):
        if n < 1000:
            return 0
        else:
            return n - 999