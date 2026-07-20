# Solution 1 - Brute Force sorting method
class Solution(object):
    def isAnagram(self, s, t):
        new_list1 = []
        new_list2 = []
        for i in range(len(s)):
            new_list1.append(s[i])
        new_list1.sort()
        for j in range(len(t)):
            new_list2.append(t[j])
        new_list2.sort()
        if new_list1 == new_list2:
            return True
        else:
            return False 