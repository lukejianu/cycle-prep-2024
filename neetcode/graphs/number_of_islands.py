# Given an m x n 2D binary grid grid which represents a map
# of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.

from itertools import product

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Returns 1 if DFS from (r, c) finds an island and 0 otherwise.
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != '1':
                return 0
            grid[r][c] = '#' # Mark as visited.
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return 1

        return sum((dfs(r, c) for r, c in product(range(m), range(n))))

