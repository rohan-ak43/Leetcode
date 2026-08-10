class Solution(object):
    def isPalindrome(self, x):
        reverse = 0
        digit = 0
        og = x
        while x>0:
            digit = x % 10
            x = x/10
            reverse = reverse * 10 + digit
        if og == reverse:
            return True
        else: 
            return False