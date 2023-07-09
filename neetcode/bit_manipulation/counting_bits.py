class Solution:
    def countBits(self, n: int) -> List[int]:
        cache = [0 for _ in range(n + 1)]
        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            cache[i] = 1 + cache[i - offset]
        return cache
