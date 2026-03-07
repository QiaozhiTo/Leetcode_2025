class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = set()
        l = 0
        for r in range(len(nums)):
            if (r - l) > k:
                d.remove(nums[l])
                l += 1
            if nums[r] in d:
                return True
            d.add(nums[r])
        return False
