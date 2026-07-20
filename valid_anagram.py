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


# Solution 2 - Using Hashmap
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!= len(t):
            return False
        hash_1 = {}
        hash_2 = {}
        for i in s:
            hash_1[i] = hash_1.get(i,0) + 1
        for j in t:
            hash_2[j] = hash_2.get(j,0) + 1
        for key in hash_1:
            if hash_1[key] != hash_2.get(key,0):
                return False
        return True