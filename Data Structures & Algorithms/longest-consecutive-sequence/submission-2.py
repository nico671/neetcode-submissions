class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for n in nums:
            if not mp[n]:
                length = mp[n-1] + mp[n+1] + 1
                mp[n] = length
                mp[n - mp[n-1]] = length
                mp[n+ mp[n+1]] = length
                res = max(res, length)
        return res