class Solution(object):
    def secondHighest(self, s):
        hasht = set()
        integer = '1234567890'
        for i in s:
            if i in integer:
                hasht.add(i)
        if len(hasht) == 1 or len(hasht) == 0:
            return -1
        else:
            new = list(hasht)
            new.sort()
            ans = new[-2]
            return int(ans)