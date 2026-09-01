class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1

        res = ""

        for c in order:
            idx = ord(c) - ord('a')
            res += c * count[idx]
            count[idx] = 0
        for i in range(26):
            res += chr(i + ord('a')) * count[i]
        return res