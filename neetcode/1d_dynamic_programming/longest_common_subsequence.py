class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcsBottomUp(text1, text2)

    def lcsTopDown(self, text1: str, text2: str) -> int:
        return self.lcsTopDownHelper(0, 0, text1, text2)

    @cache
    def lcsTopDownHelper(self, i, j, text1, text2) -> int:
        if i >= len(text1) or j >= len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + self.lcsTopDownHelper(i + 1, j + 1, text1, text2)
        return max(
                self.lcsTopDownHelper(i + 1, j, text1, text2), 
                self.lcsTopDownHelper(i, j + 1, text1, text2))

    def lcsBottomUp(self, text1: str, text2: str) -> int:
        # cache[(i, j)] = LCS in text1[i:] and text2[j:]
        cache = defaultdict(int)
        m, n = len(text1), len(text2)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    cache[(i, j)] = 1 + cache[(i + 1, j + 1)]
                else: 
                    cache[(i, j)] = max(cache[(i + 1, j)], cache[(i, j + 1)])
        return cache[(0, 0)]

