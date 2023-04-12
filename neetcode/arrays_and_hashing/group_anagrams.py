# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order. An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically using all the original
# letters exactly once.

from collections import defaultdict
from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[self.build_count_string(s)].append(s)

        return list(groups.values())

    def build_count_string(self, s) -> str:
        counts = [0] * 26
        for c in s:
            counts[ord("a") - ord(c)] += 1

        return "".join(
            [chr(ord("a") + i) + str(count) for i, count in enumerate(counts)]
        )


s = Solution()

assert s.groupAnagrams(["abc", "cab", "aab", "bac", "cat"]) == [
    ["abc", "cab", "bac"],
    ["aab"],
    ["cat"],
]

print("ALL TESTS PASS")
