class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            arr_tup = tuple(arr)
            if arr_tup in hm:
                hm[arr_tup].append(s)
            else:
                hm[arr_tup] = [s]
        return list(hm.values())