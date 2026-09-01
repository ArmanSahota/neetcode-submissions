class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = [0] * 26
        freqT = [0] * 26
        for i in s:
            freqS[ord(i) - ord('a')] += 1
        for i in t:
            freqT[ord(i) - ord('a')] += 1
        return freqS == freqT

