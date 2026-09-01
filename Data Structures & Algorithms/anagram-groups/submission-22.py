class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            if (''.join(sorted(i))) in hashmap:
                hashmap[(''.join(sorted(i)))].append(i)
            else:
                hashmap[''.join(sorted(i))].append(i)
        return list(hashmap.values())
