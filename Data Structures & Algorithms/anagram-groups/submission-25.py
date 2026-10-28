class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            sorted_strs = "".join(sorted(i))
            hashmap[sorted_strs].append(i)
        return list(hashmap.values())