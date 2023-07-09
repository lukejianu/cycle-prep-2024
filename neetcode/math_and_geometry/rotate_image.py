from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) 
        tlc = 0 # Top-left coord.
        brc = n # Bottom-right coord.
        while brc - tlc > 1: # While we have a 2x2 or bigger.
            i = 0
            new_ring = zip(self.get_ring_coords(tlc, brc), self.rotate_ring(self.get_ring(tlc, brc, matrix)))
            for (r, c), value in new_ring:
                matrix[r][c] = value
            tlc += 1
            brc -= 1

    def get_ring_coords(self, tlc, brc):
        coords = []
        # Top
        for c in range(tlc, brc):
            coords.append((tlc, c))
        # Right
        for r in range(tlc + 1, brc - 1):
            coords.append((r, brc - 1))
        # Bot
        for c in range(brc - 1, tlc - 1, -1):
            coords.append((brc - 1, c))
        # Left
        for r in range(brc - 2, tlc, -1):
            coords.append((r, tlc))
        return coords

    def rotate_ring(self, ring):
        amount = len(ring) // 4
        return ring[amount * 3:] + ring[:amount * 3] 

    def get_ring(self, tlc, brc, matrix):
        top = matrix[tlc][tlc:brc]
        right = self.get_column(brc - 1, matrix)[tlc + 1:brc - 1]
        bottom = matrix[brc - 1][tlc:brc][::-1]
        left = self.get_column(tlc, matrix)[tlc + 1:brc - 1][::-1]
        return top + right + bottom + left

    def get_column(self, c, matrix):
        return [row[c] for row in matrix]

s = Solution()
matrix = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
print(s.get_ring(0, 3, matrix))
assert s.get_ring(0, 3, matrix) == [1, 2, 3, 4, 5, 6, 7, 8]
assert s.rotate_ring(s.get_ring(0, 3, matrix)) == [7, 8, 1, 2, 3, 4, 5, 6]
print(s.get_ring_coords(0, 3))
assert s.get_ring_coords(0, 3) == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]
print('All tests pass!')

