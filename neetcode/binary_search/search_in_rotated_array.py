# There is an integer array nums sorted in ascending order with distinct values.

# Prior to being passed to your function, nums is possibly rotated at an unknown
# pivot index k (1 <= k < nums.length) such that the resulting array is:
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]. 

# For example, [0,1,2,4,5,6,7] might be rotated at pivot
# index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return
# the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # Left side is sorted.
            if nums[l] <= nums[m]: 
                if nums[l] <= target < nums[m]: 
                    r = m - 1
                else: 
                    l = m + 1
            # Right side is sorted.
            if nums[r] >= nums[m]:
                if nums[m] < target <= nums[r]: 
                    l = m + 1
                else:
                    r = m - 1

        return -1

s = Solution()

i1 = [1, 2, 3, 4, 5]
i2 = [1, 2, 3, 4, 5, 6]

assert s.search([2, 3], 3) == 1
assert s.search([4, 3], 3) == 1
assert s.search([5, 4, 1, 2, 3], 3) == 4
assert s.search([5, 4, 1, 2, 3], 4) == 1
assert s.search([5, 4, 1, 2, 3], 6) == -1
        
print('ALL TESTS PASS')
