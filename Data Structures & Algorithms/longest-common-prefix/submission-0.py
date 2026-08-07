class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        min_len = len(min(strs, key=len))
        for i in range(min_len):
            curr_char = ""
            for s in strs:
                if curr_char == "":
                    curr_char = s[i]
                    continue
                if s[i] != curr_char:
                    return "".join(res)
            res.append(curr_char)
        return "".join(res)
