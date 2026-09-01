class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isP(L, R):
            while L < R:
                if s[L].lower() != s[R].lower():
                    return False
                L += 1
                R -= 1
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].lower() != s[r].lower():
                return (isP(l, r - 1) or isP(l + 1, r))
            l += 1
            r -= 1
        return True
        