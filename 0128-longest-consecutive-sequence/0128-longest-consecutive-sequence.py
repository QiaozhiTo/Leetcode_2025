class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numsSet:
                length = 1
                while length + n in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest