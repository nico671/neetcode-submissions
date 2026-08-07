class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while len(stack):
                c_i, c_t = stack.pop()
                if c_t < t:
                    res[c_i] = i - c_i
                else:
                    stack.append((c_i, c_t))
                    break
            stack.append((i, t))
        return res