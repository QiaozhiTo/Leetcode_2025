class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+*/-':
                a, b = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)
                elif token == '/':
                    stack.append(int(b / a))
                else:
                    stack.append(a * b)
            else:
                stack.append(int(token))
        return stack[-1]
