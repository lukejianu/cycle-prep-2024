class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lengthOfLISBottomUp(nums)

    # Why does this TLE?
    def lengthOfLISTopDown(self, nums: List[int]) -> int:
        n = len(nums)
        const_nums = tuple(nums)
        return max((self.lengthOfLISHelper(i, const_nums) for i in range(n)))

    @cache
    def lengthOfLISHelper(self, i, nums) -> int:
        n = len(nums)
        longest = 1
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                longest = max(longest, 1 + self.lengthOfLISHelper(j, nums))
        return longest

    def lengthOfLISBottomUp(self, nums: List[int]) -> int:
        n = len(nums)
        # cache[i] = LIS starting at i and going till n.
        cache = [1 for _ in range(n)] 

        for i in range(n - 1, -1, -1): 
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])

        return max(cache)

