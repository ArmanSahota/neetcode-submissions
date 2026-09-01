class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            s = "".join(sorted(i))
            if s in hashmap:
                hashmap[s].append(i)
            else:
                hashmap[s].append(i)
        return list(hashmap.values())
        