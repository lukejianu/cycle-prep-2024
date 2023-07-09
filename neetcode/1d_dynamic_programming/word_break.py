class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakHelperGood(0, s, frozenset(wordDict))

    @cache
    def wordBreakHelperBad(self, s, wordDict):
        n = len(s)
        if not n:
            return True
        for i in range(n + 1):
            if s[:i] in wordDict:
                if self.wordBreakHelperBad(s[i:], wordDict):
                    return True
        return False

    @cache
    def wordBreakHelperGood(self, start, s, wordDict):
        n = len(s)
        if start >= n:
            return True
        for end in range(start, n + 1):
            if s[start:end] in wordDict:
                if self.wordBreakHelperGood(end, s, wordDict):
                    return True
        return False
        
