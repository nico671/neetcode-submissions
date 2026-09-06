class Solution:
    def trap(self, height: List[int]) -> int:
        pres = [0] * len(height)
        max_so_far = height[0]
        for i in range(1, len(height)):
            pres[i] = max_so_far
            max_so_far = max(max_so_far, height[i])
        # print(pres)
        suffs = [0] * len(height)
        max_so_far = height[-1]
        for i in range(len(height) - 2, -1 , -1):
            suffs[i] = max_so_far
            max_so_far = max(max_so_far, height[i])
        res = [0] * len(height)
        for i in range(len(height)):
            res[i] = max(0, min(pres[i], suffs[i]) - height[i])
        return sum(res)