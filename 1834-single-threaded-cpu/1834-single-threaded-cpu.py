class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t : t[0])
        i, time = 0, tasks[0][0]
        res = []
        minHeap = []

        while minHeap or i < len(tasks):
            #同一时间点可能有多个任务同时到达，用 if 只加入一个就去执行了，但应该把所有已到达的任务都加入堆再决定执行哪个。 用while而不是if
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res

            