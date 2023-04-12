# Given an array of sorted numbers, remove all duplicate number instances from
# it in-place, such that each element appears only once. The relative order of
# the elements should be kept the same and you should not use any extra space so
# that the solution has a space complexity of O(1).

# Move all the unique elements at the beginning of the array and after moving
# return the length of the subarray that has no duplicate in it.


def remove_duplicates(arr):
    n = len(arr)
    free_slot = 1
    for i in range(1, n):
        if arr[i - 1] != arr[i]:
            arr[free_slot] = arr[i]
            free_slot += 1
    return free_slot


assert remove_duplicates([1, 1, 2, 3, 3, 4]) == 4
assert remove_duplicates([1, 1, 1, 1]) == 1
assert remove_duplicates([1, 2, 3]) == 3

# Runtime:
# Trivially O(n), because of the for loop.

# Space:
# O(1), because our space usage is constant across input sizes.

# Notes:
# What does the free_slot variable really represent? One perspective is that it
# represents the barrier between confirmed non-duplicates and uncharted
# territory (we can't know for certain what is in front of us). We call it free
# slot because everything before it is a good non-duplicate (a taken slot).

# Similar Question:
# Given an unsorted array of numbers and a target ‘key’, remove all instances of
# ‘key’ in-place and return the new length of the array.


def remove_key(arr, key):
    n = len(arr)
    free_slot = 0
    for i in range(n):
        if arr[i] != key:
            arr[free_slot] = arr[i]
            free_slot += 1
    return free_slot


assert remove_key([5, 1, 1, 2], 1) == 2
assert remove_key([1, 1, 1], 1) == 0
assert remove_key([], 0) == 0

print("ASSERTIONS PASS")

# Notes:
# I struggled with these problems, because I was worried that the logic
# caused good elements (non-duplicates/non-keys) to be overwritten.
# The key observation to make here (that refutes this worry), is to notice
# the if condition. You only enter the if condition and subsequently
# take action if the current element is good. The action also ALWAYS
# involves putting the current element in a reserved slot, because
# afterwards we increment the slow pointer. So sure, you might be overwriting
# a good element, but remember that when you initially encountered that good
# element, we had already copied it into a reserved slot.
