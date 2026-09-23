class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1

        char_counts = [0] * 26
        char_counts[ord(s[l]) - ord('A')] += 1
        res = 1
        while r < len(s):

            # add s[r] to counts
            char_counts[ ord(s[r]) - ord('A')] += 1

            # window is valid when window_len - highest_single_char_count <= k
            # window_len = (r-l+1)
            # highest_single_char_count = max(char_counts)
            while (r-l+1) - max(char_counts) > k:
                char_counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
                
        return res
