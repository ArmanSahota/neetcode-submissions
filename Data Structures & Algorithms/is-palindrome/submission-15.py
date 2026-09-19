class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        while L <= R:
            if s[L].isalnum() == False:
                L += 1
                continue
            if s[R].isalnum() == False:
                R -= 1
                continue
            if s[R].lower() != s[L].lower():
                return False
            L += 1
            R -= 1
        return True
            

