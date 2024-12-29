class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            # not having duplicates 
            if nums[i-1] == nums[i] and i > 0:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 < 0:
                    l += 1
                elif sum3 > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # not having duplicates 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

# time complexity: O(N^2) + O(nlogn) -> O(N^2)[two nested array]
# space complexity: could be O(1) or O(N) sorting does take some extra spaces

