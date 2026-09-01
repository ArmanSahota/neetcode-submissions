class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        countS = {}
        for c in t: 
            countT[c] = 1 + countT.get(c, 0)
        need = len(countT)
        have = 0
        resLen, res = float('inf'), [-1, -1]

        L = 0
        for R in range(len(s)):
            c = s[R]
            countS[c] = 1 + countS.get(c, 0)
            if c in countT and countS[c] == countT[c]:
                have += 1

            while have == need:
                if (R - L + 1) < resLen:
                    resLen = R - L + 1
                    res = [L, R]
                countS[s[L]] -= 1
                if s[L] in countT and countS[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        L, R = res
        return s[L : R + 1] if resLen != float('inf') else ""
                



    

            