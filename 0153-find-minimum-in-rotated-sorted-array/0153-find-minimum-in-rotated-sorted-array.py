class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        res = max(nums)
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res
        