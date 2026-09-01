from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            newWord = ''.join(sorted(word))
            if newWord in hashmap:
                hashmap[newWord].append(word)
            else:
                hashmap[newWord].append(word)
        return list(hashmap.values())
