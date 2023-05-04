# You are given an integer array height of length n. There are n 
# vertical lines drawn such that the two endpoints of the ith line 
# are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxAreaSoFar = 0

        while l < r: 
            l_height = height[l]
            r_height = height[r]
            maxAreaSoFar = max(maxAreaSoFar, (r - l) * min(l_height, r_height))
            if l_height < r_height:
                l += 1
            else: 
                r -= 1
 
        return maxAreaSoFar

s = Solution()

assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea([1, 1]) == 1

print('ALL TESTS PASS')
        
