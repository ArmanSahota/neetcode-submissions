class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        array = set()
        result = 0
        L = 0
        for R in range(len(s)):
            while s[R] in array:
                array.remove(s[L])
                L += 1
            array.add(s[R])
            result = max(result, len(array))

        return result