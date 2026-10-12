# Solution 1
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits

# Solution 2
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0
        if i == 0:
            return [1] + digits 