class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            
            for t in dp:
                # if target == t + nums[i]:
                #     return True # runtime 271ms
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
        