class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        res = nums[0]
        for n in nums[1:]:
            tmp_min = min(n, cur_min*n, cur_max*n)
            tmp_max = max(n, cur_min*n, cur_max*n)
            cur_min, cur_max = tmp_min, tmp_max
            res = max(res, cur_max)
        return res
        