class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for ind, height in enumerate(heights):
            start = ind
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, h*(ind-i))
                start = i
            stack.append((start, height))
        
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea
            

