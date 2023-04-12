# Given an array of numbers sorted in ascending order and a target sum, find a
# pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair)
# such that they add up to the given target.


def pair_with_targetsum(arr, target_sum):
    l = 0
    r = len(arr) - 1
    while l < r:
        curr_sum = arr[l] + arr[r]
        if curr_sum == target_sum:
            return [l, r]
        elif curr_sum < target_sum:
            l += 1
        elif curr_sum > target_sum:
            r -= 1
    return [-1, -1]


assert pair_with_targetsum([1, 2, 5, 9], 7) == [1, 2]
assert pair_with_targetsum([1, 3, 5, 9, 12], 4) == [0, 1]
assert pair_with_targetsum([1, 2, 3], 6) == [-1, -1]

# Runtime:
# Trivially O(n), because of the while loop.

# Space:
# O(1), as our space usage does not depend on any of the input variables.
