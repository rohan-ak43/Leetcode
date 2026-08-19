class Solution(object):
    def isValid(self, s):
        stack = []
        dicts = { "}":"{",")":"(","]":"["}
        for i in s:
            if i in dicts:
                if not stack or stack.pop() != dicts[i]:
                    return False
            else:
                stack.append(i)
        return not stack