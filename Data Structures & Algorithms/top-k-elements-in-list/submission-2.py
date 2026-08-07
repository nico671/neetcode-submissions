class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq_map[n].append(n)
            else:
                freq_map[n] = [n]
        res = []
        for n in dict(sorted(freq_map.items(), key=lambda item: len(item[1]), reverse=True)).values():
            if len(res) >= k:
                return res
            res.append(n[0])
        return res
        