class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        res = list(counts.items())
        res = sorted(res, key=lambda x: x[1])
        res = res[-k:]
        return [x for x,y in res]