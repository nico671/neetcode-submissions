import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)
        res = max_k
        while min_k <= max_k:
            check_k = (max_k + min_k) // 2
            check_h = 0
            for n in piles:
                check_h += math.ceil(n / check_k)
            if check_h <= h:
                res = min(res, check_k)
                max_k = check_k - 1
            else:
                min_k = check_k + 1
        return res
