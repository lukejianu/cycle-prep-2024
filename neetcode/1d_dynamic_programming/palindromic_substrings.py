class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            # Odd palindromes.
            count += self.countPalindromes(i, i, s)
            # Even palindromes.
            count += self.countPalindromes(i, i + 1, s)
        return count

    def countPalindromes(self, l, r, s):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

