# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value, and the median is the mean of the two
# middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:
# - MedianFinder()
#   initializes the MedianFinder object.
# - void addNum(int num)
#   adds the integer num from the data stream to the data structure.
# - double findMedian()
#   returns the median of all elements so far. Answers 
#   within 10-5 of the actual answer will be accepted.

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Add the number to smaller heap.
        heapq.heappush(self.max_heap, -num)
        # Add the largest element in the smaller heap to the larger heap.
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # Max heap should have the same or one more element than the min heap.
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]

# Notes: 
# When both heaps are empty, we end up adding the element to the max heap. 
# On the next iteration, we add the num to the max heap, then pop the 
# largest from the max heap and add it to the min heap. This process 
# guarantees that the smaller half is in the max heap and the larger
# half is in the min heap. Afterwards, we ensure that the max heap
# either has n or n + 1 elements, where n is the size of the m in heap.

# Thus, our invariants are:
# - The top of the max_heap is <= than the top of the min_heap.
# - The max heap has n or n + 1 elements, where n is the size of the min heap.
