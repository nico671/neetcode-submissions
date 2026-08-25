class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{':'}'
        }
        
        for c in s:
            if c in mapping.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if c != mapping[last]:
                    return False

        return len(stack) == 0