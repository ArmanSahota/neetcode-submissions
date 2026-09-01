class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = len(t)
        L = 0
        for R in s:
            if L < len(t) and R == t[L]:
                L += 1
                res -= 1

        return res


