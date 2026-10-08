class Solution(object):
    def removeOuterParentheses(self, s):
        ans = []
        depth = 0
        for i in s:
            if i == '(':
                if depth > 0:
                    ans.append(i)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans.append(i)
        return "".join(ans)