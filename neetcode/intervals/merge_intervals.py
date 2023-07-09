class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        stack = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            if start <= stack[-1][1]:
                last_interval = stack.pop()
                stack.append([last_interval[0], max(last_interval[1], end)])
            else:
                stack.append([start, end])
        return stack
        
