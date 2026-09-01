class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for j in strs:
                if len(j) == i or j[i] != strs[0][i]:
                    return res
                else:
                    continue
            res += strs[0][i]
        return res
