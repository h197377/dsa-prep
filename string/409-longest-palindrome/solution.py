class Solution:
    def longestPalindrome(self, s: str) -> int:
        singles = set()
        for c in s:
            if c in singles:
                singles.remove(c)
            else:
                singles.add(c)

        if singles:
            return len(s) - len(singles) + 1
        else:
            return len(s)