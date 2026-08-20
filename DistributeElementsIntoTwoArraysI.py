class Solution(object):
    def resultArray(self, nums):
        array1 = [nums[0]]
        array2 = [nums[1]]
        for i in range(2,len(nums)):
            if array1[-1]>array2[-1]:
                array1.append(nums[i])
            else:
                array2.append(nums[i])
        return array1+array2