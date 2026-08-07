from queue import PriorityQueue 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for n in nums:
            q.put(n)
            if q.qsize() > k:
                q.get()
        return q.get()
        