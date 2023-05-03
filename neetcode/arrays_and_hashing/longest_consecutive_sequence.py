# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        # Initialize starts.
        starts = []
        for n in nums_set: 
            if n - 1 not in nums_set:
                starts.append(n)

        longest = 0
        for start in starts:
            curr = start 
            while curr + 1 in nums_set:
                curr += 1
            longest = max(longest, (curr - start) + 1)

        return longest

s = Solution()

assert s.longestConsecutive([100, 105, 1, 106, 2, 3, 102]) == 3
assert s.longestConsecutive([]) == 0

print('ALL TESTS PASS')
