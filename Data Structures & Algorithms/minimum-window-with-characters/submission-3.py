class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        have = 0
        countT = Counter(t)
        window = {}
        need = len(countT)
        res, resLen = [-1, -1], float('inf')
        L = 0
        for R in range(len(s)):
            cur = s[R]
            window[cur] = 1 + window.get(cur, 0)
            if cur in countT and window[cur] == countT[cur]:
                have += 1

            while have == need:
                if R - L + 1 < resLen:
                    res = [L, R]
                    resLen = R - L + 1

                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        L, R = res
        return s[L : R + 1] if resLen != float('inf') else ""



    

            