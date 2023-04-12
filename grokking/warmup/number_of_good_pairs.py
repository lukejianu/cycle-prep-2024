# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


class Solution:
    def numGoodPairs(self, nums):
        res = 0
        counts = dict()
        for n in nums:
            res += counts.get(n, 0)  # See Notes 1.
            counts[n] = counts.get(n, 0) + 1
        return res


s = Solution()

assert s.numGoodPairs([1, 2, 2, 3, 7, 3, 2]) == 4
assert s.numGoodPairs([1, 2, 3]) == 0

# Runtime:
# O(n), where n is the length of the input array.

# Space:
# O(n), where n is the length of the input array since we have a map.

# Notes:
# 1. We get occurences(n) new good pairs, because the current number
# forms a pair with all previous occurences.
