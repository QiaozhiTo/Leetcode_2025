class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones),heapq.heappop(stones)
            if first != second:
                new = first - second
                heapq.heappush(stones, new)
        return abs(stones[0]) if stones else 0