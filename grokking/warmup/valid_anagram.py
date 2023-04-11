# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


s = Solution()

assert s.isAnagram("care", "race") is True
assert s.isAnagram("aabbcc", "bacbac") is True
assert s.isAnagram("test", "best") is False

# Runtime:
# The runtime of this solution is O(n + m), where n is the length of one
# string and m is the length of the other. This is because creating a
# Counter object is a O(length of string) operation, since you are
# looping over the string and updating keys in a dictionary.

# Space:
# We use O(1) extra space in this solution, since the size of our dictionary
# can only be 26 characters (letters in the alphabet).
