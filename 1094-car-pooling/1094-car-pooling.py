class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1]) #o(nlog(n))
        minHeap = [] # pair of [start, numPassengers]
        curPass = 0
        for t in trips:
            numPass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            curPass += numPass

            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True
