class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for key, val in enumerate(nums):
            if (target - val) not in count:
                count[val] = key
            else:
                return [count[target-val], key]
            
                
                