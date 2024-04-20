class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        def explore_island(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
                return
            grid[row][col] = '0'  # mark as visited
            explore_island(row + 1, col)
            explore_island(row - 1, col)
            explore_island(row, col + 1)
            explore_island(row, col - 1)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    explore_island(i, j)

        return num_islands
