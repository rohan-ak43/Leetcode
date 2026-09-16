# Solution 1
class Solution(object):
    def countSegments(self, s):
        liost = s.split()
        return len(liost)

# Solution 2
class Solution(object):
    def countSegments(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i==0 or s[i-1]==' '):
                count += 1
        return count