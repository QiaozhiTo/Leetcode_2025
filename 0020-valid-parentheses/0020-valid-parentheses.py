class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if not s: return False
        for i in s:
            if i in ('{', '(', '['):
                stack.append(i)
            # need to check if stack is empty, or it will cause index out of range error
            elif stack and ((i == '}' and stack[-1] == '{') or
                            (i == ']' and stack[-1] == '[') or
                            (i == ')' and stack[-1] == '(')):
                stack.pop()
            else:
                return False


        return len(stack) == 0