class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            currSum += n
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        return maxSum

        
