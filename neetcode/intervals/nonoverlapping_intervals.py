class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[1])
        removals = 0
        latest_end = sorted_intervals[0][1]
        for start, end in sorted_intervals[1:]:
            if start < latest_end:
                removals += 1
            else:
                latest_end = end
        return removals

