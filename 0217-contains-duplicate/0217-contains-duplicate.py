# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num,0)
#         for key, val in count.items():
#             if val >1:
#                 return True
#         return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
            