class Solution(object):
    def countEven(self, num):
        ans = 0
        for i in range(1,num+1):
            digitsum = 0
            for j in str(i):
                digitsum += int(j)
            if digitsum % 2 == 0:
                ans += 1
        return ans