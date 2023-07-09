class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        for i, n in enumerate(nums):
            x = x ^ i
            x = x ^ n
        return x
        
