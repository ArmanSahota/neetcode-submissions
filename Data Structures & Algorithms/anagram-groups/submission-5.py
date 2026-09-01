from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            newWord = ''.join(sorted(word))
            hashmap[newWord].append(word)
        return list(hashmap.values())
