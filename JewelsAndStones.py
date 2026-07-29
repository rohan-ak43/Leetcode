class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hasht = set()
        count = 0
        for i in jewels:
            hasht.add(i)
        for j in stones:
            if j in hasht:
                count += 1
        return count 