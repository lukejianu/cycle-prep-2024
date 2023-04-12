# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target. You may assume that each input
# would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, n in enumerate(nums):
            goal = target - n
            if goal in seen:
                return [seen[goal], i]
            seen[n] = i

        assert False, "COULD NOT FIND A SOLUTION"


s = Solution()

assert s.twoSum([5, 2, 0, 9], 5) == [0, 2]
assert s.twoSum([1, 2], 3) == [0, 1]

print("ALL TESTS PASS")
