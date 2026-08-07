class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            hasher = tuple(counts)
            if hasher not in res:
                res[hasher] = [s]
            else:
                res[hasher].append(s)
                
        return list(res.values())