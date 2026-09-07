class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_boundaries = [len(heights) - 1] * len(heights)

        # tracks indices for which we have not seen idx j > i s.t. heights[j] > heights[i]
        stack = []

        for i in range(len(heights)):
            if not stack:
                stack.append(i)
                continue
            while stack and heights[stack[-1]] > heights[i]:
                right_boundaries[stack.pop()] = i - 1
            stack.append(i)
        # print(right_boundaries, stack)

        left_boundaries = [0] * len(heights)
        stack = []
        # for each elt, pop elements on the stack while their heights are greater
        # set right_boundaries[i] = i
        # finally, append its index to the right_boundaries stack
        for i in range(len(heights)-1, -1, -1):
            if not stack:
                stack.append(i)
                continue
            while stack and heights[stack[-1]] > heights[i]:
                left_boundaries[stack.pop()] = i + 1
            stack.append(i)
        # print(left_boundaries, stack)
        
        res = max(heights)
        for i in range(len(heights)):
            l = left_boundaries[i]
            r = right_boundaries[i]
            
            max_area = heights[i] * (r-l+1)
            # print(i,l,r, max_area)
            res = max(max_area, res)
        return res