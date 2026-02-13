class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a< 0 and stack[-1] > 0:
                diff = stack[-1] + a
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0 
                else:
                    a = 0
                    stack.pop()
            # if a => a is not 0, then append to stack
            if a:
                stack.append(a)
        return stack

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = []
#         for star in asteroids:
#             while stack and star < 0 < stack[-1]:
#                 if abs(star) > stack[-1]:
#                     stack.pop()
#                     continue # will skip the remaining code inside a loop for current iteration, so jump to 'stack.append(star)' 
#                 elif abs(star) == stack[-1]:
#                     stack.pop()
#                 break 
#             else:
#                 stack.append(star)
#         return stack

# with continue or not example:
# [-2,-2,-2,1,-2]



