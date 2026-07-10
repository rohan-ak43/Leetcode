class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            for i in range(len(haystack)):
                for j in range(len(haystack)):
                    if needle[i] in haystack[j]:
                        return i
        else:
            return -1
        