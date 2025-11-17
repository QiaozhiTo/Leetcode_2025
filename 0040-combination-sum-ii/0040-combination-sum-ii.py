class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return 
            if i == len(candidates) or total > target:
                return 
            
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            curr.pop()
           
            dfs(i+1, curr, total)
        dfs(0, [], 0)
        return res

                 
        