# Given a string s, find the length of the longest substring without repeating
# characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSoFar = 0
        window = set()
        l = 0

        for r in range(len(s)): 
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longestSoFar = max(longestSoFar, r - l + 1)

        return longestSoFar



s = Solution()

assert s.lengthOfLongestSubstring('') == 0
assert s.lengthOfLongestSubstring('a') == 1
assert s.lengthOfLongestSubstring('abbcdde') == 3

print('ALL TESTS PASS')
