class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}
        res = 0
        prev = 0
        for i in range(26):
            hashmap[keyboard[i]] = i
        for i in word:
            res += abs(prev - hashmap[i])
            prev = hashmap[i]

        return res

        