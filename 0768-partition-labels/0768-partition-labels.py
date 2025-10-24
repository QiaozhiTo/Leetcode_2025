class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastPosition = {}
        for i, v in enumerate(s):
            lastPosition[v] = i
        res = []
        size, end = 0,0
        for i, v in enumerate(s):
            size += 1
            end = max(end, lastPosition[v])

            if end == i:
                res.append(size)
                size = 0
        return res