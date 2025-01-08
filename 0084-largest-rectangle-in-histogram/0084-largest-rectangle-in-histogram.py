class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                start = ind
                maxArea = max(maxArea, height*(i-ind))
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea
            