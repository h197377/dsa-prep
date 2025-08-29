class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        hm = {} # char -> last seen idx
        res = 1
        last_non_repeat_idx = 0

        for i, c in enumerate(s):
            if c in hm:
                last_non_repeat_idx = max(last_non_repeat_idx, hm[c] + 1)
            hm[c] = i
            res = max(i - last_non_repeat_idx + 1, res)

        return res
