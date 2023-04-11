# A pangram is a sentence where every letter of the English alphabet
# appears at least once given a string sentence containing English
# letters (lower or upper-case), return true if sentence is a pangram, or false
# otherwise. Note: The given sentence might contain other characters like
# digits or spaces, your solution should handle these too.

class Solution:
    def checkIfPangram(self, sentence):
        alphabet = map(lambda x: chr(x), range(ord("a"), ord("z") + 1))
        sentence_set = set(list(sentence.lower()))
        letter_exists = map(lambda letter: letter in sentence_set, alphabet)
        return all(letter_exists)


s = Solution()
assert s.checkIfPangram("abcdefghijklmnopqrstuvwxy") is False
assert s.checkIfPangram("abcdefghijklmnopqrstuvwxyz") is True
assert s.checkIfPangram("abcdefghijklmnopqrstuvwxYz") is True
assert s.checkIfPangram(" 0_$_abcdefghijklmnopqrstuvwxyz") is True
assert s.checkIfPangram("bbcdefghijklmnopqrstuvwxyz") is False

# Runtime:
# The runtime of this solution is O(n), where n is the length of the input
# string. This is because all of our operations are linear, including
# converting a string to lowercase, then into a list, then into a set, and
# then finally mapping (looping) and then andmapping for our result.

# Space:
# The space used for this solution is O(n), where n is the length of the input
# string. This is because we use extra storage when converting to a list/set,
# and also to store the result of our map.
