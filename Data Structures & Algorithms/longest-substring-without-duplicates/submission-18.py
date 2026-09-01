class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        stack = set()
        for R in range(len(s)):
            while s[R] in stack:
                stack.remove(s[L])
                L += 1
            stack.add(s[R])
            res = max(res, R - L + 1)
        return res