class Solution(object):
    def lengthOfLastWord(self, s):
        new = s[::-1]
        splits = new.split()
        last = splits[0]
        return len(last)