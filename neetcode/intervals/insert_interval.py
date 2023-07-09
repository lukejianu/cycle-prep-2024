class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.insertTimeOpt(intervals, newInterval)

    def insertTimeOpt(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval, key=lambda interval: interval[0])
        stack = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= stack[-1][1]:
                last_interval = stack.pop()
                stack.append([last_interval[0], max(last_interval[1], end)])
            else:
                stack.append([start, end])
        return stack 

    def insertSpaceOpt(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval, key=lambda interval: interval[0])
        n = len(intervals)
        i = 1
        while i < n:
            last_interval = intervals[i - 1]
            curr_interval = intervals[i]
            if curr_interval[0] <= last_interval[1]:
                intervals[i] = [last_interval[0], max(last_interval[1], curr_interval[1])]
                intervals[i - 1] = [-1, -1]
            i += 1
        self.inplaceFilter(intervals)
        return intervals 

    def inplaceFilter(self, intervals):
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if start == -1 and end == -1:
                intervals.pop(i)
            else: 
                i += 1
        return intervals

