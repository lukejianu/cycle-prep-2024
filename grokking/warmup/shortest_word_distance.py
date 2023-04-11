# Given an array of strings words and two different strings that already exist
# in the array word1 and word2, return the shortest distance between these
# two words in the list.


class Solution:
    def shortestDistance(self, words, word1, word2):
        word1_indexes = [[i, w] for i, w in enumerate(words) if w == word1]
        word2_indexes = [[i, w] for i, w in enumerate(words) if w == word2]

        all_indexes = self.merge_lists(word1_indexes, word2_indexes)
        shortest_distance = len(words) - 1
        for i in range(len(all_indexes) - 1):
            p1 = all_indexes[i]
            p2 = all_indexes[i + 1]
            if p1[1] != p2[1]: # if the words are different
                shortest_distance = min(shortest_distance, p2[0] - p1[0])

        return shortest_distance

    def merge_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1[0][0] <= l2[0][0]:
            return [l1[0]] + self.merge_lists(l1[1:], l2)
        else:
            return [l2[0]] + self.merge_lists(l1, l2[1:])


s = Solution()
assert s.merge_lists([[1, "a"], [3, "b"]], [[2, "c"], [5, "d"]]) == [
    [1, "a"], [2, "c"], [3, "b"], [5, "d"]]
assert s.shortestDistance(["a", "b", "c", "d"], "a", "d") == 3
assert s.shortestDistance(["b", "c", "d", "b"], "b", "d") == 1

# Runtime:
# This solution is O(n), as all of our operations involve looping over the
# input word list. At one point, we also merge two sorted lists, which
# is also an O(n) operation.

# Space:
# We use O(n) space since we store indexes and other data.
