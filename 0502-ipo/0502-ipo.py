class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [[p, c] for p, c in zip(profits, capital)]
        pairs.sort(key = lambda p : p[1])
        i = 0
        maxHeap = []
        for _ in range(k):
            while i < len(pairs) and w >= pairs[i][1]:
                heapq.heappush(maxHeap, -pairs[i][0])
                i += 1
            if not maxHeap:
                break
            w += (-heapq.heappop(maxHeap))
        return w