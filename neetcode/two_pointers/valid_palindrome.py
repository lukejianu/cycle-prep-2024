# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. 

# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r: 
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            if l >= len(s) or r < 0:
                return True
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

s = Solution()

assert s.isPalindrome('abc') is False
assert s.isPalindrome('') is True
assert s.isPalindrome('#') is True
assert s.isPalindrome('r') is True
assert s.isPalindrome('racecar') is True
assert s.isPalindrome('r_!a#cecar') is True
assert s.isPalindrome('abcba') is True
assert s.isPalindrome('ab$%@#$%@ba') is True

print('ALL TESTS PASS')
