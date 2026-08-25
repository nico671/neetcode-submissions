class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ['(', '{', '[']
        closers = [')', '}', ']']
        for c in s:
            if c in openers:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last == '(' and c != ')':
                    return False
                elif last == '{' and c != '}':
                    return False
                elif last == '[' and c!= ']':
                    return False

        return len(stack) == 0

