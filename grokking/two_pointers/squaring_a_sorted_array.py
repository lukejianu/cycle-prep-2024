# Given a sorted array, create a new array containing squares of all the numbers
# of the input array in the sorted order.

from collections import deque


def make_squares(arr):
    n = len(arr)
    l = 0
    r = n - 1

    res = deque()
    while l <= r:
        l_squared = arr[l] * arr[l]
        r_squared = arr[r] * arr[r]
        if l_squared >= r_squared:
            res.appendleft(l_squared)
            l += 1
        if r_squared > l_squared:
            res.appendleft(r_squared)
            r -= 1

    return list(res)


assert make_squares([-3, 1, 0, 1, 3]) == [0, 1, 1, 9, 9]
assert make_squares([-5, 2, 0, 1, 3]) == [0, 1, 4, 9, 25]
print("ALL TESTS PASS")

# Runtime
# Trivially O(n), because of the while loop. Note that we use a deque, since
# prepending (appending left) with lists is slow.

# Space
# O(1), since our space usage is constant across input sizes. Note that we
# don't count the return list.
