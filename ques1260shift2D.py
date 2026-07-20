class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        newgrid = []
        s = len(grid[0]) - 1
        y = len(grid) - 1
        count = 0
        while count < k:
            newgrid = []
            for i in range(len(grid)):
                if i == 0:
                    newgrid.append([grid[y][s]] + grid[0][:-1])
                elif i == len(grid) - 1:
                    newgrid.append([grid[y-1][s]] + grid[y][:-1])
                else:
                    newgrid.append([grid[i-1][s]] + grid[i][:-1])
            grid = newgrid
            count += 1
        return grid