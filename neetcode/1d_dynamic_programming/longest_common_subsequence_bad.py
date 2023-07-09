class StringView:
    def __init__(self, s, li, ri):
        self.s = s
        self.li = li
        self.ri = ri

    def getString(self):
        return s[l:r + 1]

    def lc(self): 
        return self.s[self.li]

    def rc(self): 
        return self.s[self.ri]

    def shiftLeft(self):
        return StringView(self.s, self.li + 1, self.ri)

    def shiftRight(self):
        return StringView(self.s, self.li, self.ri - 1)

    def __len__(self):
        return self.ri - self.li + 1

    def __bool__(self):
        return len(self) > 0

    # Do these need to be defined?
    def __hash__(self):
        return hash((self.s, self.li, self.ri))

    # Is this implementation correct?
    def __eq__(self, other):
        return self.s == other.s and self.li == other.li and self.ri == other.ri

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceTopDown(text1, text2)

    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        sv1 = StringView(text1, 0, len(text1) - 1)
        sv2 = StringView(text2, 0, len(text2) - 1)
        return self.longestCommonSubsequenceTopDownHelper(sv1, sv2)

    @cache
    def longestCommonSubsequenceTopDownHelper(self, sv1, sv2) -> int:
        if not sv1 or not sv2:
            return 0
        if sv1.lc() == sv2.lc(): 
            return 1 + self.longestCommonSubsequenceTopDownHelper(sv1.shiftLeft(), sv2.shiftLeft())
        if sv1.rc() == sv2.rc(): 
            return 1 + self.longestCommonSubsequenceTopDownHelper(sv1.shiftRight(), sv2.shiftRight())
        return max(
                self.longestCommonSubsequenceTopDownHelper(sv1.shiftLeft(), sv2),
                self.longestCommonSubsequenceTopDownHelper(sv1.shiftRight(), sv2),
                self.longestCommonSubsequenceTopDownHelper(sv1, sv2.shiftLeft()),
                self.longestCommonSubsequenceTopDownHelper(sv1, sv2.shiftRight()))

