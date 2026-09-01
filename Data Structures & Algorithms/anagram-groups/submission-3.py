from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            if word in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key].append(word)
        return list(hashmap.values())