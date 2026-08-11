class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num2 = str(num)
            numnew = 0
            for i in num2:
                numnew += int(i)
            num = numnew
        return num