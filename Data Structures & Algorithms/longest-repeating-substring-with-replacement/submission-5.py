class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = [0] * 26
        l = 0
        res = 0
        repl = 0
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            seen[idx] += 1
            repl = sum(seen) - max(seen)
            while repl > k and l < r:
                l_idx = ord(s[l]) - ord('A')
                seen[l_idx] -= 1
                repl = sum(seen) - max(seen)
                l += 1
            res = max(res, r - l + 1)
        return res
