class Solution(object):
    def countDigits(self, num):
        nums = str(num)
        count = 0
        for i in nums:
            if num % int(i) == 0:
                count += 1
        return count