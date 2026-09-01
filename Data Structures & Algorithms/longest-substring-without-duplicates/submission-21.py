class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        last = {}
        for R in range(len(s)):
            if s[R] in last:
                L = max(L, last[s[R]] + 1)
            last[s[R]] = R
            res = max(res, R - L + 1)
        return res
