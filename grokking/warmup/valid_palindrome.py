# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non - alphanumeric characters, it
# reads the same forward and backward. Alphanumeric characters include
# letters and numbers. Given a string s, return true if it is a
# palindrome, or false otherwise.

class Solution:
    def is_palindrome(self, s):
        cleaned_s = [c for c in s.lower() if ord("a") <= ord(c) <= ord("z")]
        return cleaned_s[::-1] == cleaned_s


s = Solution()

assert s.is_palindrome("test") is False
assert s.is_palindrome("racecar") is True
assert s.is_palindrome("R_a c__eCa/]R") is True

# Runtime:
# This solution is O(n), where n is the length of the input string.
# This is because our operations involve a loop over the input,
# and a simple reverse of a string.

# Space:
# This solution uses O(n) extra space, because we have to store the cleaned
# string in memory, as well as the reversed string, both of which scale
# linearly with the size of the input string.
