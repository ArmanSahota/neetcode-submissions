class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        res = 1
        for i in range(len(s)-1, 0, -1):
            if s[i] != " ":
                j = i - 1
                while s[j].isalpha():
                    res +=1
                    j -= 1               
            else: continue 
            return max(res, 1)
