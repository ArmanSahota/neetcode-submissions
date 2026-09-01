class Solution:
    def scoreOfString(self, s: str) -> int:
        L= 0
        cur = 0
        for r in range(1, len(s)):            
            cur = cur + (abs(ord(s[r]) - ord(s[L])))
            print(cur)
            L += 1
        return cur
            
        