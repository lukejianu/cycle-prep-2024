# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        counts_inversed = [[-v, k] for k, v in counts.items()]
        heapq.heapify(counts_inversed)
        return [n for _, n in heapq.nsmallest(k, counts_inversed)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for n, count in counts.items():
            buckets[count].append(n)

        for bucket in buckets[::-1]:
            for n in bucket:
                if len(result) == k:
                    return result
                result.append(n)

        return result


s = Solution()

assert s.topKFrequent([1, 1, 1, 3, 2, 2], 2) == [1, 2]
assert s.topKFrequent([1, 2, 3], 3) == [1, 2, 3]

print("ALL TESTS PASS")
