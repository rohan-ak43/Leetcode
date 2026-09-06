class Solution(object):
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        left, right = 2, num//2
        while left <= right:
            mid = (left + right)//2
            sqnum = mid * mid
            if sqnum == num:
                return True
            elif sqnum > num:
                right = mid - 1
            else:
                left = mid + 1
        return False