from queue import PriorityQueue 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = PriorityQueue()
        for s in stones:
            q.put(-s)
        while q.qsize() > 1:
            s1 = -q.get()
            s2 = -q.get()
            if s1 == s2:
                continue
            elif s1 < s2:
                q.put(-(s2-s1))
            else:
                q.put(-(s1-s2))
        if q.qsize():
            return -q.get()
        return 0