class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        length = 0
        for R in s:
            while R in window:
                window.remove(s[L])
                L += 1
            window.add(R)
            length = max(length, len(window))
        return length
            