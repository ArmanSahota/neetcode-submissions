class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isP (L, R):
            while L < R:
                if s[L].lower() != s[R].lower():
                    return False
                L += 1
                R -= 1
            return True
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L].lower() != s[R].lower():
                return (isP(L + 1, R) or isP(L, R - 1))
            L += 1
            R -= 1
        return True