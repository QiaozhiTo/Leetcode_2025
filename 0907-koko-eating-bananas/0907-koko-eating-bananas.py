class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            m = (l+r)//2
            total_time = 0
            for p in piles:
                 total_time += math.ceil(float(p)/m)
            if total_time > h:
                l = m + 1
            else:
                r = m -1
                res= min(m, res)
        return res