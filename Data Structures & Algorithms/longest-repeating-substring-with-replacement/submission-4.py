class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        L = 0
        res = 0
        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)
            while (R - L + 1) - max(window.values()) > k:
                window[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res

