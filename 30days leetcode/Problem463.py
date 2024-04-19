class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        perimeter, rows, cols = 0, len(grid), len(grid[0])
        extended_grid = [row + [0] for row in grid] + [[0] * (cols + 1)]
        for i in range(rows):
            for j in range(cols):
                if extended_grid[i][j] == 1:
                    perimeter += 4 - 2 * (extended_grid[i + 1][j] + extended_grid[i][j + 1])

        return perimeter
