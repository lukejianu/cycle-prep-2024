# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


s = Solution()
assert s.containsDuplicate([1, 2, 3]) is False
assert s.containsDuplicate([1, 1]) is True
assert s.containsDuplicate([]) is False
assert s.containsDuplicate([1, 2, 1]) is True

# Runtime:
# The runtime of this solution is O(n), where n is the length of the input
# list. This is because converting a list to a set is O(n), as we have
# to loop over the entire list to add those elements to the set.

# Space:
# The space used in this solution is also O(n), since we create a set, which
# in the worst case, has all n elements in it (when there are no dups).
