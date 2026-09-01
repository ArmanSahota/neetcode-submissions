class Solution:
    def isPalindrome(self, s: str) -> bool:
        R = len(s) -1
        L = 0
        while L < R:
            s = s.lower()
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1
        return True

