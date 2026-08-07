class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}
        for s in strs:
            sort_s = str(sorted(s))
            if sort_s in h_map.keys():
                h_map[sort_s].append(s)
            else:
                h_map[sort_s] = [s]
        return list(h_map.values())
        