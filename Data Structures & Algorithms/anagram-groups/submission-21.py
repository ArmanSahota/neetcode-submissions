class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            s = "".join(sorted(i))
            hashmap[s].append(i)
        return list(hashmap.values())
        