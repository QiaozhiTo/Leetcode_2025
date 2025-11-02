class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm, res = [], []
        def dfs(perm:List[int], pick:List[bool]):
            if len(nums) == len(perm):
                res.append(perm[:])
                return 
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(perm, pick)
                    perm.pop()
                    pick[i] = False
        dfs([], [False]*len(nums))
        return res
