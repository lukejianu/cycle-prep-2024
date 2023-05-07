# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum
# element of this array.

# You must write an algorithm that runs in O(log n) time.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minSoFar = nums[0]

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            # Left side is sorted.
            if nums[l] <= nums[m]: 
                minSoFar = min(minSoFar, nums[l])
                l = m + 1
            # Right side is sorted.
            elif nums[r] >= nums[m]: 
                minSoFar = min(minSoFar, nums[m])
                r = m - 1

        return minSoFar

s = Solution() 

i1 = [1, 2, 3, 4, 5]
i2 = [1, 2, 3, 4, 5, 6]

assert s.findMin([4, 5, 1, 2, 3]) == 1
assert s.findMin([4, 5, 6, 1, 2, 3]) == 1

assert s.findMin([2, 3, 4, 5, 1]) == 1

print('ALL TESTS PASS')
