class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p, s] for p,s in zip(position, speed)]
        for (x,y) in reversed(sorted(pair)):
            stack.append((target-x)/y)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        