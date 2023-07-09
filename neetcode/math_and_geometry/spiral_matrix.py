class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        return self.spiralOrderHelper(0, 0, m, n, matrix)

    def spiralOrderHelper(self, tlr, tlc, brr, brc, matrix):
        # No grid.
        if tlr >= brr or tlc >= brc:
            return []
        # 1xn grid.
        if brr - tlr == 1:
            return matrix[tlr][tlc:brc]
        # nx1 grid.
        if brc - tlc == 1:
            return [matrix[r][tlc] for r in range(tlr, brr)]
        ordering = []
        r, c = tlr, tlc
        # Move right.
        while c < brc - 1: 
            ordering.append(matrix[r][c])
            c += 1
        # Move down.
        while r < brr - 1: 
            ordering.append(matrix[r][c])
            r += 1
        # Move left.
        while c > tlc: 
            ordering.append(matrix[r][c])
            c -= 1
        # Move up.
        while r > tlr: 
            ordering.append(matrix[r][c])
            r -= 1
        return ordering + self.spiralOrderHelper(tlr + 1, tlc + 1, brr - 1, brc - 1, matrix)

