class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0 
        hashmap = {}
        res = 0
        for R in range(len(s)):
            if s[R] in hashmap:
                L = max(L, hashmap[s[R]] + 1)
            hashmap[s[R]] = R
            res = max(res, R - L + 1)
        return res
