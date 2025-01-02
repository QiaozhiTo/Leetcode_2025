# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         digits = []
#         for ele in tokens:
#             if ele not in '+-*/':
#                 digits.append(int(ele))
#             else:
#                 num1 = digits.pop()
#                 num2 = digits.pop()
#                 if ele == '+':
#                     digits.append(num2 + num1)
#                 if ele == '-':
#                     digits.append(num2 - num1)
#                 if ele == '*':
#                     digits.append(num2 * num1)
#                 if ele == '/':
#                     digits.append(int(num2 / num1))
              
#         return digits[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for each in tokens:
            if each == '+':
                stack.append(stack.pop()+stack.pop())
            elif each == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif each == '*':
                stack.append(stack.pop()*stack.pop())
            elif each == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(each))
        return stack[0]
                
