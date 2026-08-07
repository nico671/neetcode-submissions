class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        together = list(zip(position, speed))
        sorted_together = sorted(together, key=lambda x: x[0])
        stack = []
        for pos, speed in sorted_together:
            print(pos, speed)
            time = (target - pos) / speed
            while len(stack) > 0 and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)