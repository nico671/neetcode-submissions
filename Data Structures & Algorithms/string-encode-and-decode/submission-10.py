class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # str_len = len(s)
            curr = str(len(s)) + "#" + s
            res += curr
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            curr_len = ""
            while s[i] != "#":
                curr_len += s[i]
                i += 1
            curr_len = int(curr_len)
            
            curr_str = ""
            for j in range(i+1, i+curr_len+1):
                curr_str += s[j]
            res.append(curr_str)
            i = i+curr_len+1
        return res