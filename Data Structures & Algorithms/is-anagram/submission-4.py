class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = []
        for i in s:
            hashmap.append(i)
        print (hashmap)
        for i in t:
            if i not in hashmap:
                return False
            else: hashmap.remove(i)

        return True
