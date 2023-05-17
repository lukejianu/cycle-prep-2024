# Given an m x n board of characters and a list of strings words, return all
# words on the board.

# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.

class TrieNode:
    def __init__(self): 
        self.characters = dict()
        self.end = False
        self.word = ''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Initialize trie.
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.characters:
                    curr.characters[c] = TrieNode()
                curr = curr.characters[c]
            curr.end = True
            curr.word = word

        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = []
        def dfs(r, c, curr): 
            if curr.end: 
                result.append(curr.word)
                curr.end = False
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            if board[r][c] in curr.characters: 
                temp = board[r][c]
                board[r][c] = '#' # To avoid cycles.
                for dr, dc in directions:
                    dfs(r + dr, c + dc, curr.characters[temp])
                board[r][c] = temp

        for r in range(m): 
            for c in range(n): 
                dfs(r, c, root)

        return result
