class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        L = 0
        res = 0

        for R in range(len(s)):
            if s[R] in hashmap:
                L = max(hashmap[s[R]] + 1, L)
            hashmap[s[R]] = R
            res = max(res, R - L + 1)
        return res
                





