class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for s in strs:
            s_counter = Counter(s)

            found = False
            for key in hashmap:
                if Counter(key) == s_counter:
                    hashmap[key].append(s)
                    found = True
                    break
            
            if not found:
                hashmap[s] = [s]
        return list(hashmap.values())