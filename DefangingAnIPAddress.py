class Solution(object):
    def defangIPaddr(self, address):
        ans = ""
        for i in address:
            if i == ".":
                ans += "[.]"
            else:
                ans += i
        return ans