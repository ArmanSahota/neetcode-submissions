class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        L = 0
        res = 0
        for R in range(len(s)):
            if s[R] in window:
                L = max(L, window[s[R]] + 1)
            window[s[R]] = R
            res = max(res, R - L + 1)
            
            
        return res



        