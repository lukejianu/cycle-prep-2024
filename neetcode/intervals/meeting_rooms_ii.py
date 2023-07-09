class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return self.minMeetingRoomsOpt(intervals)

    def minMeetingRoomsHeap(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0]) # O(nlogn)
        meetings = [] # Heap
        max_rooms = 0
        for start, end in sorted_intervals:
            while meetings and meetings[0] <= start: # Meeting has ended.
                heapq.heappop(meetings)
            heapq.heappush(meetings, end)
            max_rooms = max(max_rooms, len(meetings))
        return max_rooms

    def minMeetingRoomsOpt(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        starts = [interval[0] for interval in sorted(intervals, key=lambda interval: interval[0])]
        ends = [interval[1] for interval in sorted(intervals, key=lambda interval: interval[1])]
        rooms = max_rooms = 0
        i = j = 0 # i and j represent indices in starts and ends (respectively).
        while i < n:
            if starts[i] < ends[j]: # Meeting has started.
                i += 1
                rooms += 1
                max_rooms = max(max_rooms, rooms)
            else: # Meeting has ended.
                rooms -= 1
                j += 1
        return max_rooms

# Reflection:
# Both solutions are O(nlogn) runtime because of the sorting, and use O(n) extra space.
# I failed to solve this problem because I failed to make the observation that the 
# intervals as a whole are irrelevant, and instead the focus is on the start/end times.

