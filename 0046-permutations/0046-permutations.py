class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, perm, pick):
            if len(perm) == len(pick):
                res.append(perm[:])
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(nums, perm, pick)
                    perm.pop()
                    pick[i] = False
        dfs(nums, [], [False]*len(nums))
        return res