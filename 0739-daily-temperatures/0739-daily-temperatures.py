class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0]*len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res