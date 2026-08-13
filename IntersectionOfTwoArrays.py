class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        new = []
        for i in set1:
            if i in set2:
                new.append(i)
        return new