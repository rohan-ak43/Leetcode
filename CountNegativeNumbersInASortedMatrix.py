class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in grid[i]:
                if j < 0:
                    count += 1
        return count