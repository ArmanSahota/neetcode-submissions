from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            sWord = "".join(sorted(word))
            if sWord in count:
                count[sWord].append(word)
            else:
                count[sWord].append(word)
        return list(count.values()) 