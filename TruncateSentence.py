class Solution(object):
    def truncateSentence(self, s, k):
        liost = s.split()
        string = " ".join(liost[:k])
        return string