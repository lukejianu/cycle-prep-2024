# Given an array of unsorted numbers, find all unique triplets in it that add up
# to zero.


def search_triplets(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    triplets = []
    for i in range(n - 2):
        if i > 0 and sorted_arr[i - 1] == sorted_arr[i]:
            continue

        target = -sorted_arr[i]
        l, r = i + 1, n - 1
        while l < r:
            curr_sum = sorted_arr[l] + sorted_arr[r]
            if curr_sum < target:
                l += 1
            if curr_sum > target:
                r -= 1
            if curr_sum == target:
                triplets.append([sorted_arr[i], sorted_arr[l], sorted_arr[r]])
                l += 1
                while l < n and sorted_arr[l - 1] == sorted_arr[l]:
                    l += 1

    return triplets


assert search_triplets([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
print("ALL TESTS PASS")

# Runtime:
# O(n^2), because for every element, we perform an O(n) two sum search.

# Space:
# O(1), since our space usage is constant across input sizes. We ignore the
# output.

# Notes:
# The main difficulty in this problem is avoiding the duplicates. The strategy
# we take here is to never use the same pivots. Since we sort the input,
# the duplicates are all next to one another, which makes skipping over them
# easier. It's key to pick the first duplicate, instead of picking the last
# one. This means that if you have a an array [..., 3, 3, 3, ...], we want
# to always pivot on the leftmost 3, and skip over the ones that come after.
# We do this because we want to maximize the search space between pivots.
