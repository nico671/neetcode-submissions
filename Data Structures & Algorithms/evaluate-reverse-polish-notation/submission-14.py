class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            elif token == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
       
        return stack.pop()