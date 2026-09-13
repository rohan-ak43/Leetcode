class Solution(object):
    def checkIfPangram(self, sentence):
        alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if len(sentence) < 26:
            return False
        for i in range(26):
            if alp[i] not in sentence:
                return False
        return True