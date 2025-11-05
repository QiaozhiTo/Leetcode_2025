class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # rob1 rob2 1 2 3 1
        for n in nums:
            tmp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         for i in range(len(nums)-3, -1, -1):
#             nums[i] += max(nums[i+2:])
#         return max(nums)
