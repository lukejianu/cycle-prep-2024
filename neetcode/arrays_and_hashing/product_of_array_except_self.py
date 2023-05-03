# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.

# You must write an algorithm that runs in O(n) time and without using
# the division operation.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfixProducts = [1 for _ in range(len(nums))]
        
        # The PP at i is equal to the PP at (i + 1) * (number at i)
        # because we simply want to include the excluded.
        for i in range(len(nums) - 2, -1, -1):
            postfixProducts[i] = postfixProducts[i + 1] * nums[i + 1]
        
        prefixProduct = 1
        for i in range(len(nums)):
            postfixProducts[i] = prefixProduct * postfixProducts[i]
            prefixProduct *= nums[i]

        return postfixProducts

s = Solution()

assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

print('ALL TESTS PASS')
        
