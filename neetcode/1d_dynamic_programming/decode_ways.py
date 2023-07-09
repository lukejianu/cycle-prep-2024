class Solution:
    def numDecodings(self, s: str) -> int:
        return self.numDecodingsOpt(s)

    @cache
    def numDecodingsTrivial(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 1
        if s[0] == "0": 
            return 0
        if n == 1:
            return 1
        if int(s[:2]) <= 26:
            return self.numDecodingsTrivial(s[1:]) + self.numDecodingsTrivial(s[2:])
        return self.numDecodingsTrivial(s[1:])

    def numDecodingsOpt(self, s):
        return self.numDecodingsOptHelper(0, s)

    @cache
    def numDecodingsOptHelper(self, i, s):
        n = len(s)
        if i >= n:
            return 1
        if s[i] == "0": 
            return 0
        res = self.numDecodingsOptHelper(i + 1, s)
        if i + 1 < n and int(s[i:i+2]) <= 26:
            res += self.numDecodingsOptHelper(i + 2, s)
        return res

