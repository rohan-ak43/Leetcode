class Solution(object):
    def reverseString(self, s):
        right = 0
        left = len(s) - 1
        while right<=left:
            s[right], s[left] = s[left], s[right]
            right += 1
            left -=1
        return s 