class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # append (val, min_of_stack_at_push_time)
        if not self.stack:
            self.stack.append((val, val))
        else:
            curr_min = self.getMin()
            self.stack.append((val, min(val,curr_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
