class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        string1 = ""
        string2 = ""
        for i in word1:
            string1 += i
        for j in word2:
            string2 += j
        if string1 == string2:
            return True
        else:
            return False