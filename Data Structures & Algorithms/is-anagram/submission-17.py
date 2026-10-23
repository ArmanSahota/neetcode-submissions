class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freq = [0] * 26
        #print(freq)
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        if max(freq) > 0 or min(freq) < 0:
            return False
        return True
