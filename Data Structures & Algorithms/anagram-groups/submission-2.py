from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            if key in hashmap:
                hashmap[key].append(i)
            else:
                hashmap[key].append(i)
        return list(hashmap.values())
