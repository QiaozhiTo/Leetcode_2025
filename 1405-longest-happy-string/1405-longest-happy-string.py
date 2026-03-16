class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                # we dont have any secondary char, can't add any more characters
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2: #if count2 != 0
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count: # if count != 0
                heapq.heappush(maxHeap, (count, char))
        return res

