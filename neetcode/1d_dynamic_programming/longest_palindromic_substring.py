class Longest:
    def __init__(self, s):
        if len(s) == 0: 
            assert False, "String cannot be empty!"
        self.l = 0
        self.r = 1
        self.s = s

    # Update the indices if the provided indices represent a longer string.
    def tryUpdate(self, l, r):
        if r - l > self.r - self.l:
            self.l = l
            self.r = r

    # Get the longest string.
    def getString(self):
        return self.s[self.l:self.r]
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindromeOpt(s)

    # Runtime: O(n^2)
    # Space: O(1)
    def longestPalindromeOpt(self, s: str) -> str:
        n = len(s)
        longest = Longest(s)

        for i in range(n):
            # Odd palindromes.
            odd_l, odd_r = self.palindromeIndices(i, i, s)
            longest.tryUpdate(odd_l, odd_r + 1)
            # Even palindromes.
            even_l, even_r = self.palindromeIndices(i, i + 1, s)
            longest.tryUpdate(even_l, even_r + 1)

        return longest.getString()

    def palindromeIndices(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (l + 1, r - 1)

    # Runtime: O(n^2)
    # Space: O(n^2)
    def longestPalindromeDp(self, s: str) -> str:
        # dp[r][c] = isPalindrome(s[r:c])
        n = len(s) + 1
        dp = [[None] * n for _ in range(n)]
        for r in range(n - 1):
            dp[r][r + 1] = True 
            dp[r][r] = True 
        
        longest = Longest(s) 
        for c in range(n):
            for r in range(c):
                if c - r > 1 and s[r] == s[c - 1]:
                    if dp[r + 1][c - 1]:
                        dp[r][c] = True
                        longest.tryUpdate(r, c) 

        return longest.getString()

s = Solution()
print(s.longestPalindrome("aba"))
assert s.longestPalindrome("cababd") == "aba"
print('All tests pass!')

