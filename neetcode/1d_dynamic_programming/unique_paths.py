from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathsBottomUp(m, n)
        
    def uniquePathsTopDown(self, m: int, n: int) -> int:
        return self.uniquePathsTopDownHelper(0, 0, m, n)

    @cache
    def uniquePathsTopDownHelper(self, r, c, m, n) -> int:
        if r < 0 or c < 0 or r >= m or c >= n:
            return 0
        if r == m - 1 and c == n - 1:
            return 1
        return self.uniquePathsTopDownHelper(r + 1, c, m, n) + self.uniquePathsTopDownHelper(r, c + 1, m, n) 

    def uniquePathsBottomUp(self, m: int, n: int) -> int:
        corner = (m - 1, n - 1)
        # cache[(r, c)] = number of ways to get to (r, c) from corner.
        cache = dict([(corner, 1)])
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r, c) == corner:
                    continue
                cache[(r, c)] = cache.get((r + 1, c), 0) + cache.get((r, c + 1), 0)
        return cache[(0, 0)]

s = Solution()
assert s.uniquePathsBottomUp(3, 7) == 28

