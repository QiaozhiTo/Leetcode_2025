class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))
        
    def rob_linear(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2