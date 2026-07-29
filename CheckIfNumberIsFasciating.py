class Solution(object):
    def isFascinating(self, n):
        hasht = {}
        a = 2*n
        b = 3*n
        c = a * b
        count = 1
        for i in str(c):
            hasht[i] = count
        #if '0' in hasht:
        #    return False
        #elif count ==1:
        #    return True
        #else:
        #    return False
        return hasht
print(Solution().isFascinating(192))