from itertools import product

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Every cell will contain:
        # - the height.
        # - a boolean representing whether you can reach it from the Atlantic.
        # - a boolean representing whether you can reach it from the Pacific.
        for r in range(m):
            for c in range(n):
                height = heights[r][c]
                heights[r][c] = [height, False, False] 

        def dfs(r, c, i): 
            if r < 0 or c < 0 or r >= m or c >= n or heights[r][c][i]:
                return
            heights[r][c][i] = True
            for dr, dc in directions: 
                new_r, new_c = r + dr, c + dc
                if new_r >= 0 and new_c >= 0 and new_r < m and new_c < n:
                    # Since we inverted the problem, the water flows upwards.
                    if heights[new_r][new_c][0] >= heights[r][c][0]:
                        dfs(new_r, new_c, i)

        # Pacific West
        for r in range(m):
            dfs(r, 0, 1)

        # Pacific North
        for c in range(n):
            dfs(0, c, 1)

        # Atlantic East
        for r in range(m):
            dfs(r, n - 1, 2)

        # Atlantic South
        for c in range(n):
            dfs(m - 1, c, 2)

        return ([r, c] for r, c in product(range(m), range(n)) if all(heights[r][c][1:]))

