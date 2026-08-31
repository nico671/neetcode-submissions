class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + ((r-l) // 2)
            curr_time = 0
            for pile in piles:
                # add time for single pile at this k
                curr_time += math.ceil(pile / k)
            
            if curr_time > h:
                l = k + 1
            if curr_time <= h:
                res = min(res, k)
                r = k - 1
            print(res, k, curr_time)
        return res