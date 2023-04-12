# Given an array of unsorted numbers and a target number, find a triplet in the
# array whose sum is as close to the target number as possible, return the sum
# of the triplet. If there are more than one such triplet, return the sum of the
# triplet with the smallest sum.


def triplet_sum_close_to_target(arr, target_sum):
    n = len(arr)
    sorted_arr = sorted(arr)
    closest_sum_so_far = float("inf")

    for i in range(n - 2):
        curr_target = target_sum - sorted_arr[i]
        curr_sum = sorted_arr[i] + two_sum_close_to_target(
            sorted_arr, i + 1, curr_target
        )
        curr_distance = abs(curr_sum - target_sum)
        closest_distance = abs(closest_sum_so_far - target_sum)
        if curr_distance <= closest_distance:
            if curr_distance == closest_distance:
                closest_sum_so_far = min(closest_sum_so_far, curr_sum)
            else:
                closest_sum_so_far = curr_sum

    return closest_sum_so_far


# Given a sorted array, a start index to search from, and a target, returns the
# two sum closest to the target.
def two_sum_close_to_target(arr, start, target_sum):
    n = len(arr)
    l, r = start, n - 1
    closest_sum_so_far = float("inf")

    while l < r:
        curr_sum = arr[l] + arr[r]
        curr_distance = abs(curr_sum - target_sum)
        closest_distance = abs(closest_sum_so_far - target_sum)
        if curr_distance <= closest_distance:  # We've found a better pair.
            if curr_distance == closest_distance:
                closest_sum_so_far = min(closest_sum_so_far, curr_sum)
            else:
                closest_sum_so_far = curr_sum
        if curr_sum < target_sum:
            l += 1
        if curr_sum > target_sum:
            r -= 1
        if curr_sum == target_sum:
            return curr_sum

    return closest_sum_so_far


assert two_sum_close_to_target([-1, 0, 2, 5, 9], 0, 9) == 9
assert two_sum_close_to_target([-5, -1, -1, 0, 2, 3, 11], 0, 8) == 6
assert two_sum_close_to_target([-10, -1, -1, 0, 2, 3, 11], 0, 8) == 10

assert triplet_sum_close_to_target([-1, 0, 2, 3], 3) == 2
assert triplet_sum_close_to_target([-3, -1, 1, 2], 1) == 0
assert triplet_sum_close_to_target([1, 0, 1, 1], 100) == 3
assert triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5) == 4

print("ALL TESTS PASS")
