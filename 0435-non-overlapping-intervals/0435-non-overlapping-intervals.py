class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd <= start:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res