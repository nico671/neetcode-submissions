class Solution:
    def isValid(self, s: str) -> bool:
        openers = "{(["
        closers = "]})"
        stack = []
        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                if len(stack) < 1:
                    return False
                curr = stack.pop()
                checker = ""
                match c:
                    case ")":
                        checker = "("
                    case "}":
                        checker = "{"
                    case "]":
                        checker = "["
                if curr != checker:
                    return False
            else:
                print("unexpected") 
        return len(stack) == 0