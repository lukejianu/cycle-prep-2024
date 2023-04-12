# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator


class Solution:
    def mySqrt(self, x):
        l, r = 0, x + 1
        closest_so_far = 0
        while l < r:
            m = (l + r) // 2
            if m * m == x:
                return m
            if m * m > x:
                r = m
            if m * m < x:
                closest_so_far = max(closest_so_far, m)
                l = m + 1
        return closest_so_far


s = Solution()
assert s.mySqrt(9) == 3
assert s.mySqrt(8) == 2
assert s.mySqrt(1) == 1
assert s.mySqrt(0) == 0

# Runtime:
# The runtime of this solution is O(log(n)), where n is the given integer.
# This is because we are performing binary search on the range(0, n).

# Space:
# The space of this solution is O(1), since as our input grows, we still
# are using the same amount of local variables.
