class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1
        print (count)
        res = ""
        for i in order:
            if i in s:
                res += (i *  count[ord(i) - ord('a')])
        for i in s:
            if i not in res:
                res += (i * count[ord(i) - ord('a')])
        return res