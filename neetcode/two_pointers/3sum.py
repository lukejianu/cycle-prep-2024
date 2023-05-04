# Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)

        triplets = []
        for i in range(n - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            target = -sorted_nums[i]
            while l < r:
                two_sum = sorted_nums[l] + sorted_nums[r]
                if two_sum < target:
                    l += 1
                elif two_sum > target:
                    r -= 1
                else: 
                    triplets.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1

                    while l < n - 1 and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1

        return triplets

s = Solution()

assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
print('ALL TESTS PASS')
