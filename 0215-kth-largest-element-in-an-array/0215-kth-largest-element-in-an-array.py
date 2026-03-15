class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]      
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(l, r):
            i = l
            rand = randint(l,r)
            nums[rand], nums[r] = nums[r], nums[rand]
            pivot = nums[r]
            for j in range(l,r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            
            if i == len(nums)-k:
                return nums[i]
            elif i > len(nums)-k:
                return quick_sort(l, i)
            else:
                return quick_sort(i+1, r)
        return quick_sort(0, len(nums)-1)
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        for i in nums:
            heappush(min_heap,i)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
'''    
           