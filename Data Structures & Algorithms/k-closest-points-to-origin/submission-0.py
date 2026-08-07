from queue import PriorityQueue 
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = PriorityQueue()
        dist_map = {}
        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt((x**2)+(y**2))
            q.put(dist)
            if dist not in dist_map:
                dist_map[dist] = [p]
            else:
                dist_map[dist].append(p)
        res = []
        for i in range(k):
            res.append(dist_map[q.get()].pop(0))
        return res