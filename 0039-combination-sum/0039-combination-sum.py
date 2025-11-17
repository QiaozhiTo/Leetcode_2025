class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i, total):
            if sum(curr) == target:
                res.append(curr[:])
                return 
            if i == len(candidates) or total > target:
                return 
            curr.append(candidates[i])
            dfs(i, total + candidates[i])
            curr.pop()
            dfs(i + 1, total)
        dfs(0, 0)
        return res

        