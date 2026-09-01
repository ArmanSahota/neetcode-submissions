class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        L = 0
        Result = 0
        for R in range(len(s)):
            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1
            hashset.add(s[R])
            Result = max(Result, R - L + 1)
        return Result
