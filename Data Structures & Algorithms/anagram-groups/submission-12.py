class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            k = "".join(sorted(i))
            hashmap[k].append(i)
        return list(hashmap.values())