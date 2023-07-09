class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_row = any(c == 0 for c in matrix[0])
        zero_col = any(row[0] == 0 for row in matrix)
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if zero_row: # Zero the 0th row.
            for c in range(n):
                matrix[0][c] = 0

        if zero_col: # Zero the 0th col.
            for r in range(m):
                matrix[r][0] = 0
        
