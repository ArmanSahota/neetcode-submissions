class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sorted_strs = "".join(sorted(i))
            if sorted_strs not in hashmap:
                hashmap[sorted_strs] = []
            hashmap[sorted_strs].append(i)
        return list(hashmap.values())