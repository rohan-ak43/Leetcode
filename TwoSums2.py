class Solution(object):
    def twoSum(self, numbers, target):
        first = 0
        last = len(numbers) - 1
        while first < last:
            sums = numbers[first] + numbers[last]
            if sums == target:
                return [first+1, last+1]
            elif sums < target:
                first += 1
            else:
                last -= 1
        