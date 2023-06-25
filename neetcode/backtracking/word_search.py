# Given an m x n grid of characters board and a string word, return true if word
# exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where
# adjacent cells are horizontally or vertically neighboring. The same letter
# cell may not be used more than once.

from itertools import product

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, i): 
            if i >= len(word): 
                return True
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            if board[r][c] == word[i]:
                cell = board[r][c]
                board[r][c] = '#'
                for dr, dc in directions:
                    if dfs(r + dr, c + dc, i + 1): 
                        return True
                board[r][c] = cell
            return False
        return any((dfs(r, c, 0) for r, c in product(range(m), range(n))))


        
