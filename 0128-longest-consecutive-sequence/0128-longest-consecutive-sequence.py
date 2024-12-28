class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        longest = 0
        for n in numsSet:
            if (n-1) not in numsSet:
                length = 0
                while length + n in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numsset = set(nums)
#         longest = 0
#         for n in nums:
#             if (n-1) not in numsset:
#                 length = 0
#             while (n+length) in numsset:
#                 length += 1
#             longest = max(length, longest)
#         return longest

# class Solution(object):
#     def longestConsecutive(self, nums):
#         nums.sort()
#         longest = 0

#         for i in range(1, len(nums)):
#             length = 0
#             while (nums[i-1] + 1) == nums[i]:
#                 length += 1
#             longest = max(longest, length)
#         return longest