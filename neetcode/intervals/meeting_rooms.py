class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        return self.canAttendMeetingsGood(intervals)

    def canAttendMeetingsGood(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda interval: interval[0])
        return all((not self.isOverlapping(intervals[i], intervals[i + 1]) for i in range(n - 1)))

    def isOverlapping(self, i1, i2):
        return i1[1] > i2[0] # i1 ends after i2 starts.

    def canAttendMeetingsBad(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda interval: interval[0])
        for i in range(1, n):
            last_interval = intervals[i - 1]
            curr_interval = intervals[i]
            if curr_interval[0] < last_interval[1]:
                return False
        return True
        
