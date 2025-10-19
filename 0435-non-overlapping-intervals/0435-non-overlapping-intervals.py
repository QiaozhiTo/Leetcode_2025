class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # not overlapping with next, update the prevEnd
            if prevEnd <= start:
                prevEnd = end
            else:
            # overlapping, remove the one with larger end(the longer interval)
                res += 1
                prevEnd = min(prevEnd, end)
        return res