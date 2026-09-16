class Solution(object):
    def mostWordsFound(self, sentences):
        maxi = 0
        for i in range(len(sentences)):
            word = sentences[i].split()
            if len(word) > maxi:
                maxi = len(word)
        return maxi