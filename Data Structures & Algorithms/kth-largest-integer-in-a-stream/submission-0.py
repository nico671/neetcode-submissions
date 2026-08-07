class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.queue.append(val)
        self.queue = sorted(self.queue)
        return self.queue[-self.k]