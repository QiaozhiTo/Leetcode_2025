class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}
        for ind, val in enumerate(nums):
            if target - val not in count:
                count[val] = ind
            else:
                return [count[target-val], ind]
    
        