class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Count = Counter(tasks)
        maxHeap = [-cnt for cnt in Count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: # check cnt not 0
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])
        return time
        