class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")":"(", "}":"{", "]":"["}
        for each in s:
            if each not in parentheses:
                stack.append(each)
            elif stack and stack[-1] == parentheses[each]:
                stack.pop()
            else:
                return False
            
        return True if not stack else False
