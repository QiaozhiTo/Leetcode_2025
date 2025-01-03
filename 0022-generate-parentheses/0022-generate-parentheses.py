class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []
        def backtrack(left, right):
            if left == right == n:
                res.append("".join(stack))
                return 
            if left < n:
                stack.append("(")
                backtrack(left+1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(left, right+1)
                stack.pop()
        backtrack(0,0)
        return res


        