# You are given a string s and an integer k. You can choose any character of the
# string and change it to any other uppercase English character. You can perform
# this operation at most k times.

# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        longestSoFar = 0
        l = 0

        for r in range(len(s)):
            window[s[r]] += 1

            # While our window is invalid...
            while max(window.values()) + k < (r - l + 1):
                window[s[l]] -= 1
                l += 1

            longestSoFar = max(longestSoFar, r - l + 1)

        return longestSoFar

s = Solution()

assert s.characterReplacement('', 6) == 0
assert s.characterReplacement('abcdef', 6) == 6
assert s.characterReplacement('abccbb', 2) == 5

print('ALL TESTS PASS')
