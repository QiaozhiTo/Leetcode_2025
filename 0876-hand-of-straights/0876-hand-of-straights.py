class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        if len(hand) % groupSize:
            return False
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            for i in range(minHeap[0], minHeap[0] + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
