class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        delta = defaultdict(int)
        for a, b in trust:
            delta[a] -= 1
            delta[b] += 1
            
        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i