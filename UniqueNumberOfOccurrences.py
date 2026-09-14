class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}
        for i in arr:
            count[i] = count.get(i,0)+1
        occ = list(count.values())
        sets = set(occ)
        if occ == sets:
            return True
        else:
            return False