# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is
# included in the window. If there is no such substring, return
# the empty string "".

# The testcases will be generated such that the answer is unique.

from collections import Counter
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_needed = Counter(t)
        minWindowSubstring = ''
        l = 0

        for r in range(len(s)):
            # Update chars needed.
            if s[r] in chars_needed:
                chars_needed[s[r]] -= 1
            
            # Shrink window if possible.
            while all([c <= 0 for c in chars_needed.values()]): 
                # Update minimum. 
                if not minWindowSubstring or (r - l + 1) < len(minWindowSubstring):
                    minWindowSubstring = s[l:r + 1]

                # Shrink and update chars needed.
                if s[l] in chars_needed:
                    chars_needed[s[l]] += 1
                l += 1
            
        return minWindowSubstring

s = Solution()

assert s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'

print('ALL TESTS PASS')

