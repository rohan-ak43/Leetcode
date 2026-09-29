class Solution(object):
    def halvesAreAlike(self, s):
        a = ""
        b = ""
        for i in range(len(s)/2):
            a += s[i]
        for j in range(len(s)/2,len(s)):
            b += s[j]
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count1 = 0
        count2 = 0
        for i in a:
            if i in vow:
                count1 += 1
        for j in b:
            if j in vow:
                count2 += 1
        if count1 == count2:
            return True
        else:
            return False