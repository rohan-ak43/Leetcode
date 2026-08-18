class Solution(object):
    def intersect(self, nums1, nums2):
        count = {}
        for i in nums1:
            count[i] = count.get(i,0)+1
        result = []
        for j in nums2:
            if count.get(j,0)>0:
                result.append(j)
                count[j] -= 1
        return result