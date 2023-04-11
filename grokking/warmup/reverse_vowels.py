# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
# lower and upper cases, more than once.

VOWELS = "aeiou"


class Solution:
    def reverseVowels(self, s):
        vowel_indices = [i for i, c in enumerate(s) if c.lower() in VOWELS]
        swap_pairs = self.generate_swap_pairs(vowel_indices)
        ret = list(s)
        for v1, v2 in swap_pairs:
            ret[v1] = s[v2]
            ret[v2] = s[v1]

        return "".join(ret)

    def generate_swap_pairs(self, indices):
        n = len(indices)
        return [[indices[i], indices[-(i + 1)]] for i in range(n // 2)]


s = Solution()
assert s.reverseVowels("hello") == "holle"
assert s.reverseVowels("cry") == "cry"
assert s.reverseVowels("test") == "test"
assert s.reverseVowels("hellO") == "hOlle"

# Runtime:
# This solution is O(n), where n is the length of the input string. This is
# because our solution involves a constant number of loops.input

# Space:
# This solution uses O(n) space, where n is the length of the input string.
# This is because we store the vowel indices, swap pairs, and generate our
# return value, which all scale linearly with the size of the string.
