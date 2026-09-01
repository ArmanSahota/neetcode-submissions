class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        l = 0
        res = 0
        for r in range(len(t)):
            if t[r] == s[l] and l < len(s):
                res += 1
                l += 1
            if res == len(s):
                return True
            

        return res == len(s)


        