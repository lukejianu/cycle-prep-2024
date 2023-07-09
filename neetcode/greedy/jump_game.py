class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1 # The last index.
        i = n - 2 # The current index.

        while target > 0 and i >= 0:
            if i + nums[i] >= target:
                target = i # We just need to get to i.
            i -= 1

        return target == 0
        
