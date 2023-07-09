class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod_so_far = max(nums)
        max_prod = min_prod = 1
        for n in nums:
            if n == 0:
                max_prod = min_prod = 1
                continue
            old_max_prod = max_prod
            max_prod = max(max_prod * n, min_prod * n, n)
            min_prod = min(min_prod * n, old_max_prod * n, n)
            max_prod_so_far = max(max_prod_so_far, max_prod)
        return max_prod_so_far

# Key Observation: 
#   - The max/min prods represent the max/min of a subarray ending at
#   the previous n in nums.

